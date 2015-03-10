# Create your models here.
from django.db import models

class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')