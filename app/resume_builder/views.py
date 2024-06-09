from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render

@login_required
def index(request):
    return render(request, "resume_builder/index.html")
