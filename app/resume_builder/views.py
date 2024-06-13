# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.views.generic import (TemplateView, ListView)
from .models import Timeline_Event, Timeline_Event_Detail
from .forms import TimelineForm
# from accounts.models import CustomUser

class Index(LoginRequiredMixin, ListView):
    model = Timeline_Event
    template_name = "resume_builder/index.html"    

    def get_queryset(self):
        print(self.request.user.id)
        return Timeline_Event.objects.filter(user_id=self.request.user.id)


class Editor(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/editor.html"


class Download(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"
