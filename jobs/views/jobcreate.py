from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.views.generic import CreateView

from ..models import Job


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = "jobcreate.html"
    fields = (
        "title",
        "description",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.type == 'faculty':
            # Redirect to a page indicating permission denied or handle it accordingly
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("403 Forbidden")
