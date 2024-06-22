from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, ListView, TemplateView, UpdateView)


from .forms import TimelineForm, TimelineDetailForm
from .models import Timeline_Event, Timeline_Event_Detail


class Index(LoginRequiredMixin, ListView):
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


class Editor(LoginRequiredMixin, CreateView):
    model = Timeline_Event
    form_class = TimelineForm
    template_name = "resume_builder/editor.html"
    success_url = "/resume/editor/"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline"] = Timeline_Event.objects.filter(user_id=self.request.user.id)
        return context
  
    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Event added to timeline",
        )
        return super().form_valid(form) # Saves the form
    

class UpdateCompany(LoginRequiredMixin, UpdateView):    
    model = Timeline_Event
    form_class = TimelineForm
    template_name = "resume_builder/update_company.html"
    success_url = "/resume/editor/"

    def get_object(self, queryset=None):
        return Timeline_Event.objects.get(pk=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_details"] = Timeline_Event_Detail.objects.filter(
            timeline_event_id=self.kwargs["pk"], user_id=self.request.user.id
            )
        return context


class UpdateDetails(LoginRequiredMixin, UpdateView):
    model = Timeline_Event_Detail
    form_class = TimelineDetailForm
    template_name = "resume_builder/update_company.html"
    success_url = "/resume/company/"

    def get_object(self, queryset=None):
        return Timeline_Event_Detail.objects.get(pk=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_details"] = Timeline_Event_Detail.objects.filter(
            timeline_event_id=self.kwargs["pk"], user_id=self.request.user.id
            )
        return context

class Download(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"
