from django.urls import path
# from django.views.generic import TemplateView
from resume_builder import views

app_name = "resume_builder"

urlpatterns = [
    # resume/
    path("", views.IndexView.as_view(), name="index"),
    path("editor/", views.EditorView.as_view(), name="editor"),
    path("editor/company/<int:pk>/", views.UpdateCompanyView.as_view(), name="update_company"),
    path("editor/details/new/", views.CreateDetailsView.as_view(), name="create_details"),
    path("editor/details/<int:pk>/", views.UpdateDetailsView.as_view(), name="update_details"),
    path("download/", views.DownloadView.as_view(), name="download"),
]