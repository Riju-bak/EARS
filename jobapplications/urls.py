from django.urls import path

from jobapplications.views import JobApplicationListView, JobApplicationCreateView, JobApplicationDetailView, \
    JobApplicationUpdateView, JobApplicationDeleteView

urlpatterns = [
    path("", JobApplicationListView.as_view(), name="jobapplication_list"),
    path("new/", JobApplicationCreateView.as_view(), name="jobapplication_create"),
    path("<int:pk>/", JobApplicationDetailView.as_view(), name="jobapplication_detail"),
    path("<int:pk>/edit/", JobApplicationUpdateView.as_view(), name="jobapplication_edit"),
    path("<int:pk>/delete/", JobApplicationDeleteView.as_view(), name="jobapplication_delete"),
]
