from django.urls import path
from . import views

app_name = "resume_builder"

urlpatterns = [
    # resume/
    path("", views.index, name="index"),
    path("update/", views.update_resume, name="update_resume"),
    path("download/", views.download, name="download"),
]