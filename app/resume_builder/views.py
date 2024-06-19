# from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, CreateView)


from .forms import TimelineForm
from .models import Timeline_Event, Timeline_Event_Detail


class Index(LoginRequiredMixin, ListView):
    model = Timeline_Event
    template_name = "resume_builder/index.html"

    # def get_queryset(self):
    #     context = Timeline_Event.objects.filter(
    #         user_id=self.request.user.id,
    #         timeline_event_detail__user_id=self.request.user.id,
    #     ).order_by("-timeline_start_date")
    #     return context

    def get_queryset(self):
        context = Timeline_Event.objects.filter(
            user_id=self.request.user.id,
            timeline_event_detail__user_id=self.request.user.id,
        ).order_by("-timeline_start_date")
        return context


class Editor(LoginRequiredMixin, CreateView):
    model = Timeline_Event
    form_class = TimelineForm
    template_name = "resume_builder/editor.html"
    success_url = "/resume/editor/"
    
    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Event sandwich added to timeline",
        )
        return super().form_valid(form)


class Download(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"
