from django.urls import path
from . import views

app_name = "resume_builder"

urlpatterns = [
    # resume/
    path("", views.index, name="index"),
    path("editor/", views.editor, name="editor"),
    path("download/", views.download, name="download"),
]