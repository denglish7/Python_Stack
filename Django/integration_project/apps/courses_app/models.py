from __future__ import unicode_literals
from django.db import models
from ..login_and_registration_app.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    student = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
