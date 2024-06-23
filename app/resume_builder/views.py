from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, ListView, 
                                  TemplateView, UpdateView)

# Imports for reportlab
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO


from .forms import TimelineForm, TimelineDetailForm
from .models import Timeline_Event, Timeline_Event_Detail


class IndexView(LoginRequiredMixin, ListView):
    model = Timeline_Event
    template_name = "resume_builder/index.html"

    def get_queryset(self):     
        queryset = Timeline_Event.objects.filter(
            user_id=self.request.user.id
            ).order_by("-timeline_start_date"
            )
        context = []
        for item in queryset:
            details = []
            qs = Timeline_Event_Detail.objects.filter(timeline_event_id=item.pk)
            for detail in qs:
                details.append(
                    detail.content
                ) 
            context.append({
                "pk": item.pk,
                "role": item.role_name,
                "company": item.org_name,
                "start_date": item.timeline_start_date,
                "end_date": item.timeline_end_date,
                "content": details,               
            })        
        return context


class EditorView(LoginRequiredMixin, CreateView):
    model = Timeline_Event
    form_class = TimelineForm
    template_name = "resume_builder/editor.html"
    success_url = "/resume/editor/"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline"] = Timeline_Event.objects.filter(
            user_id=self.request.user.id
            ).order_by(
                "org_name"
            )
        return context

    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Event added to timeline",
        )
        return super().form_valid(form) # Saves the form


class UpdateCompanyView(LoginRequiredMixin, UpdateView):    
    model = Timeline_Event
    form_class = TimelineForm
    template_name = "resume_builder/update_company.html"
    success_url = "/resume/editor/"

    # Retrieves form data from database
    def get_object(self, queryset=None):
        return Timeline_Event.objects.get(pk=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_details"] = Timeline_Event_Detail.objects.filter(
            timeline_event_id=self.kwargs["pk"], user_id=self.request.user.id
            )
        context["company_id"] = self.kwargs["pk"]
        self.request.session["company_event_id"] = self.kwargs["pk"]
        print("pk:", self.request.session["company_event_id"])
        # Context incldues the table id / primary key for the company (event)
        return context
    
    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Company/role updated",
        )
        return super().form_valid(form) # Saves the form
    

class DeleteCompanyView(LoginRequiredMixin, DeleteView):
    model = Timeline_Event
    template_name = "resume_builder/delete_company.html"

    def get_success_url(self):
        return reverse("resume_builder:editor")


class CreateDetailsView(LoginRequiredMixin, CreateView):
    model = Timeline_Event_Detail
    form_class = TimelineDetailForm
    template_name = "resume_builder/create_details.html"    

    def get_success_url(self):
        return reverse("resume_builder:update_company", kwargs={"pk": self.request.session["company_event_id"]})

    def get_form_initial_data(self):
        initial = {}
        initial["timeline_details"] = Timeline_Event_Detail.objects.filter(
            # id=self.kwargs["event_id"],
            user_id=self.request.user.id,
            )
        
        # Make event id /company id directly accessbible in context without looping
        initial["timeline_event_id"] = self.request.session["company_event_id"]
        # Context includes the table id / primary key for the detail used in back navigation
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_form_initial_data())
        print("transfer: ", self.request.session["company_event_id"])
        return context
   
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        initial_data = self.get_form_initial_data()
        kwargs["initial"] = {**kwargs.get("initial", {}), **initial_data}
        return kwargs
    
    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Detail added",
        )
        return super().form_valid(form) # Saves the form


class UpdateDetailsView(LoginRequiredMixin, UpdateView):
    model = Timeline_Event_Detail
    form_class = TimelineDetailForm
    template_name = "resume_builder/update_details.html"

    def get_success_url(self):
        return reverse("resume_builder:update_company", kwargs={"pk": self.request.session["company_event_id"]})

    # Retrieves form data from database
    def get_object(self, queryset=None):
        return Timeline_Event_Detail.objects.get(pk=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_details"] = Timeline_Event_Detail.objects.filter(
            id=self.kwargs["pk"],
            user_id=self.request.user.id,
            )
        # Make event id /company id directly accessbible in context without looping
        context["company_id"] = context["timeline_details"][0].timeline_event_id_id
        print(self.request.session["company_event_id"])
        # Context includes the table id / primary key for the detail used in back navigation
        return context
    
    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Detail updated",
        )
        return super().form_valid(form) # Saves the form
    

class DeleteDetailsView(LoginRequiredMixin, DeleteView):
    model = Timeline_Event_Detail
    template_name = "resume_builder/delete_details.html"

    def get_success_url(self):
        return reverse("resume_builder:update_company", kwargs={"pk": self.request.session["company_event_id"]})


class DownloadView(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"


def get_txt(request):
    response = HttpResponse(content_type="text/plain")
    response["Content-Disposition"] = "attachement; filename=resume.txt"

    # lines = ["line 1\n", "line 2\n"]

    queryset = Timeline_Event.objects.filter(
        user_id=request.user.id
        ).order_by("-timeline_start_date"
        )
    experience = []
    for item in queryset:
        details = []
        qs = Timeline_Event_Detail.objects.filter(timeline_event_id=item.pk)
        for detail in qs:
            details.append(
                detail.content
            ) 
        experience.append({            
            "role": item.role_name,
            "company": item.org_name,
            "start_date": item.timeline_start_date,
            "end_date": item.timeline_end_date,
            "content": details,               
        }) 
    
    lines = []
    full_name = f"{request.user.first_name} {request.user.last_name}"
    lines.append(f"{full_name}\n\n")

    for role in experience:
        for key, value in role.items():
            if key == "content":
                for bullet in value:                    
                    lines.append(f"  - {bullet}\n")
            else:                
                lines.append(f"{value}\n")
        lines.append("\n")

    # Write to txt file
    response.writelines(lines)
    return response


def get_pdf(request):
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    c = canvas.Canvas(buffer, pagesize=letter)

    # Get data from your ListView
    # items = YourModel.objects.all()  # Adjust this query as needed
        
    queryset = Timeline_Event.objects.filter(
        user_id=request.user.id
        ).order_by("-timeline_start_date"
        )
    context = []
    for item in queryset:
        details = []
        qs = Timeline_Event_Detail.objects.filter(timeline_event_id=item.pk)
        for detail in qs:
            details.append(
                detail.content
            ) 
        context.append({            
            "role": item.role_name,
            "company": item.org_name,
            "start_date": item.timeline_start_date,
            "end_date": item.timeline_end_date,
            "content": details,               
        }) 
        

    # Draw things on the PDF
    y = 750  # Starting y position
    for item in context:
        c.drawString(20, y, f"{item}: {item}")  # Adjust fields as needed
        y -= 20  # Move down by 20 points

    # Close the PDF object cleanly, and we're done
    c.showPage()
    c.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='output.pdf')
