from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from .models import GroupMember,Group
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model=Group
    
class SingleGroup(LoginRequiredMixin,generic.DetailView):
    model=Group
    
class ListGroups(LoginRequiredMixin,generic.ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request, *args, **kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        
        except IntegrityError:
            messages.warning(request,'Warning already a member!')
        else:
            messages.success(request,'You are now a member')
        
        return super().get(request,*args,**kwargs)
    
class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
        
    def get(self,request,*args, **kwargs):
        try:
            membership=GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except GroupMember.DoesNotExist:
            messages.warning(request,'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success(request,'You have left this gouop')
        return super().get(request,*args,**kwargs)