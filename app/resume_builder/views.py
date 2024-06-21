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
    #     return Timeline_Event.objects.filter(
    #         user_id=self.request.user.id,
    #         timeline_event_detail__user_id=self.request.user.id,
    #         ).order_by("-timeline_start_date")

    # def get_queryset(self):     
    #     return Timeline_Event_Detail.objects.select_related("timeline_event_id")

    def get_queryset(self):     
        queryset = Timeline_Event.objects.filter(user_id=self.request.user.id)
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
    
    def form_valid(self, form): # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms
        form.instance.user_id = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Event added to timeline",
        )
        return super().form_valid(form)


class Download(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"
