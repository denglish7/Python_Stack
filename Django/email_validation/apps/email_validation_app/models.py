from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
    def add_email(self, data):
        errors = []

        if not EMAIL_REGEX.match(data['email_address']):
            errors.append("Invalid email address")

        response = {}

        if not errors:
            new_email = self.create(email=data['email_address'])
            response['added'] = True
            response['new_email'] = new_email
        else:
            response['added'] = False
            response['errors'] = errors

        return response


class Email(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmailManager()
# Create your models here.
