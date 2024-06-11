from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, get_object_or_404, render
from .models import Timeline_Event, Timeline_Event_Detail
from accounts.models import CustomUser

@login_required
def index(request):    
    events = 1
    context = {
        "timeline": events
    }
    return render(request, "resume_builder/index.html", context)

@login_required
def editor(request):
    return render(request, "resume_builder/editor.html")

@login_required
def download(request):
    return render(request, "resume_builder/download.html")
