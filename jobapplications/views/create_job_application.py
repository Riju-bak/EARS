from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.views.generic import CreateView

from jobapplications.models import JobApplication


class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    template_name = "jobapplication_create.html"
    fields = (
        "job",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.type == 'applicant':
            return super().dispatch(request, *args, **kwargs)
        else:
            # Redirect to a page indicating permission denied or handle it accordingly
            return HttpResponseForbidden("403 Forbidden: Only applicants may create a job application")
