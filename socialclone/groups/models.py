from enum import unique
from typing import OrderedDict
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.
from django import template
register=template.Library()

User=get_user_model()

class Group(models.Model):
    name=models.CharField(max_length=255, unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    description=models.TextField(blank=True,default='')
    member=models.ManyToManyField(User,through='GroupMember',related_name='ugroups')
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})
    
    class Meta:
        ordering=['name']
    
        
class GroupMember(models.Model):
    group=models.ForeignKey(Group,on_delete=models.PROTECT,related_name='groups')
    user=models.ForeignKey(User, on_delete=models.PROTECT,related_name='user_groups')
    
    def __str__(self):
        return f'User: {self.user.username} Group: {self.group.name}'
     
    class Meta:
        unique_together =['group','user']