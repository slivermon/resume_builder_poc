from django.contrib.auth.forms import (AuthenticationForm)
from django.shortcuts import HttpResponse, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def landingpage(request):
    if request.method == "POST":
        return HttpResponse("Logged in landing page")
    
    else:
        form = AuthenticationForm
        context = {"form": form}
        print(context)
        return render(request, "index.html", context)
