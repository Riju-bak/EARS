from django.conf import settings
from django.db import models
from django.urls import reverse

from jobs.models.job import Job


class JobApplication(models.Model):
    job = models.ForeignKey(Job, related_name="applications", on_delete=models.CASCADE)
    body = models.TextField()  # TODO: Figure out how to put placeholder text in forms
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobapplication_detail", kwargs={"pk": self.pk})
