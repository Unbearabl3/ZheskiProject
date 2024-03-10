from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    # UserName = models.CharField('UserName', max_length=32)
    # Password = models.CharField('Password', max_length=32)
    # Email = models.EmailField('Email')

