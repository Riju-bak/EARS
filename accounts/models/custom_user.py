from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Type(models.TextChoices):
        FACULTY = 'faculty'
        APPLICANT = 'applicant'

    type = models.CharField(choices=Type.choices, max_length=20)
