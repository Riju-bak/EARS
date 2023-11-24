from django.conf import settings
from django.db import models
from django.urls import reverse

from . import JobApplication


class Comment(models.Model):
    jobapplication = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("jobapplication_list")
