from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import JobApplication


class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = "jobapplication_list.html"
