from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

from jobapplications.models import JobApplication


class JobApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JobApplication
    fields = (
        "body",
    )
    template_name = "jobapplication_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
