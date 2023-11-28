from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from jobs.models import Job


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = "jobdetail.html"
