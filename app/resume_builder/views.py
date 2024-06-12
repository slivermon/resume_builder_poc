# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.views.generic import (TemplateView)
# from .models import Timeline_Event, Timeline_Event_Detail
from .forms import TimelineForm
# from accounts.models import CustomUser

class Index(TemplateView):
    template_name = "resume_builder/index.html"
    # events = 1
    # context = {
    #     "timeline": events
    # }
    # render(request, "resume_builder/index.html", context)

class Editor(TemplateView):
    template_name = "resume_builder/editor.html"

# @login_required
# def editor(request):
#     if request.method == "POST":
#         return HttpResponse("POST to editor/")
#     else:
#         context = {}
#         context["form"] = TimelineForm()
#         return render(request, "resume_builder/editor.html", context)

class Download(LoginRequiredMixin, TemplateView):
    template_name = "resume_builder/download.html"
