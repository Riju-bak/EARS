from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from jobapplications.models import JobApplication


class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    template_name = "jobapplication_create.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
