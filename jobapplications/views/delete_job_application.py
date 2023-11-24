from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from jobapplications.models import JobApplication


class JobApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobApplication
    template_name = "jobapplication_delete.html"
    success_url = reverse_lazy("jobapplication_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
