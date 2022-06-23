from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

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