from django.db import models


class Registration(models.Model):
    UserName = models.CharField('Username', max_length=32)
    Password = models.CharField('Password', max_length=32)
    Email = models.EmailField('Email')
class Authorization(models.Model):
    UserName = models.CharField('Username', max_length=32)
    Password = models.CharField('Password', max_length=32)
# Create your models here.
