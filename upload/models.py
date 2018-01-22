from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from hr.storage_backends import PrivateMediaStorage


# Create your models here.
def upload_to_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=upload_to_path)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PrivateDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=PrivateMediaStorage())
    user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)