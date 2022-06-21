from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
# Create your models here.


class UserInfo(User):
    profile_pic=models.ImageField(null=True, blank=True,upload_to='profile_pics')
    def __str__(self):
        return f'@{self.username}'