from __future__ import unicode_literals

from django.db import models

class Movie(request):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Actor(request):
    first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    movies = models.ManyToManyField(Movie)
    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
