from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from ..forms import CommentForm
from ..models import JobApplication


class CommentGet(DetailView):
    model = JobApplication
    template_name = "jobapplication_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = JobApplication
    form_class = CommentForm
    template_name = "jobapplication_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.jobapplication = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        jobapplication = self.get_object()
        return reverse("jobapplication_detail", kwargs={"pk": jobapplication.pk})
