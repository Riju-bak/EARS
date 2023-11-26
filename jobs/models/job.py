from django.conf import settings
from django.db import models
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobdetail", kwargs={"pk": self.pk})
