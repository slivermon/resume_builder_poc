from django.urls import path
from . import views

app_name = "resume_builder"

urlpatterns = [
    # resume/
    path("", views.index, name="dashboard"),
]