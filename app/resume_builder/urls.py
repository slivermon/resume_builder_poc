from django.urls import path
# from django.views.generic import TemplateView
from resume_builder import views

app_name = "resume_builder"

urlpatterns = [
    # resume/
    path("", views.Index.as_view(), name="index"),
    path("editor/", views.Editor.as_view(), name="editor"),
    path("editor/company/<int:pk>/", views.UpdateCompany.as_view(), name="update_company"),
    path("editor/details/<int:pk>/", views.UpdateDetails.as_view(), name="update_details"),
    path("download/", views.Download.as_view(), name="download"),
]