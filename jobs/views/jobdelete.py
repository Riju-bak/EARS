from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from jobs.models import Job


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = "jobdelete.html"
    success_url = reverse_lazy("joblist")

    def test_func(self):
        obj = self.get_object()
        return self.request.user.type == 'faculty'
