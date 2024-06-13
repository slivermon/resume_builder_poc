from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, CreateView)


from .forms import TimelineForm


from .models import Timeline_Event


class Index(LoginRequiredMixin, ListView):
    model = Timeline_Event
    template_name = "resume_builder/index.html"

    def get_queryset(self):
        print(self.request.user.id)
        return Timeline_Event.objects.order_by("-timeline_start_date").filter(user_id=self.request.user.id)


class Editor(LoginRequiredMixin, CreateView):
    model = Timeline_Event
    form_class = TimelineForm
    template_name = "resume_builder/editor.html"    
    
    # TODO: Remove this once forms.py is confirmed to work well.
    # fields = [
    #     "timeline_start_date",
    #     "timeline_end_date",
    #     "org_name",
    #     "role_name",
    #     "org_type",
    # ]   

    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Event added to timeline",
        )
        return super().form_valid(form)


class Download(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"
