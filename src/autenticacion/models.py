from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from requests import delete
# Create your models here.


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)
