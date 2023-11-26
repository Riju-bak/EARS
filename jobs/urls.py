from django.urls import path

from jobs.views import JobListView, JobCreateView, JobDetailView, \
    JobUpdateView, JobDeleteView

urlpatterns = [
    path("", JobListView.as_view(), name="joblist"),
    path("new/", JobCreateView.as_view(), name="jobcreate"),
    path("<int:pk>/", JobDetailView.as_view(), name="jobdetail"),
    path("<int:pk>/edit/", JobUpdateView.as_view(), name="jobedit"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="jobdelete"),
]
