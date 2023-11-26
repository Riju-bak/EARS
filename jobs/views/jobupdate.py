from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from jobs.models import Job


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = (
        "title",
        "description",
    )
    template_name = "jobedit.html"
    success_url = reverse_lazy('joblist')

    def test_func(self):
        obj = self.get_object()
        return self.request.user.type == 'faculty'
