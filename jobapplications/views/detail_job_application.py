from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .comment import CommentGet, CommentPost


class JobApplicationDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)