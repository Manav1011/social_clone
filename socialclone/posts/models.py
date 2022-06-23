from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model
# Create your models here.

User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_posts')
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField(blank=False,null=False)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='group_posts',null=True,blank=True)
    
    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("post:single", kwargs={"username": self.user.username,'pk':self.pk})
    
    class Meta:
        ordering=['created_at']
        unique_together=['user','message']
        