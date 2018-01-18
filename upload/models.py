from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from hr.storage_backends import PrivateMediaStorage


# Create your models here.

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class PrivateDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=PrivateMediaStorage())
    user = models.ForeignKey(User, related_name='documents', on_delete=True)