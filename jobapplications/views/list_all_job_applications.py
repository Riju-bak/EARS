from urllib.parse import urlparse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from ..models import JobApplication


class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = "jobapplication_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        author_pk = self.request.GET.get('author')

        if author_pk:
            queryset = queryset.filter(author__pk=author_pk)

        return queryset

    def dispatch(self, request, *args, **kwargs):
        if request.user.type == 'applicant':
            # Check if the current URL already contains the 'author' query parameter
            current_url = request.get_full_path()
            parsed_url = urlparse(current_url)
            query_params = parsed_url.query

            if 'author' not in query_params:
                current_url = current_url[:len(current_url) - 1]
                # Redirect to the applications authored by the applicant
                return redirect(f'{current_url}?author={request.user.pk}')

        return super().dispatch(request, *args, **kwargs)
