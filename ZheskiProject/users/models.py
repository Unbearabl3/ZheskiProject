from django.db import models


class Users(models.Model):
    UserName = models.CharField('Username', max_length=32)
    Password = models.CharField('Password', max_length=32)
    Email = models.EmailField('Email')

    def __str__(self):
        return self.UserName
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
