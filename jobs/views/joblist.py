from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from jobs.models import Job


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = "joblist.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        author_pk = self.request.GET.get('author')

        if author_pk:
            queryset = queryset.filter(author__pk=author_pk)

        return queryset