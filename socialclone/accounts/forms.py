from django import forms
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        model=models.UserInfo
        fields=('username', 'email','password1','password2','profile_pic')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Display name'
        self.fields['email'].label='Email address'
        self.fields['password1'].label='Password'
        self.fields['password2'].label='Confirm password'
        self.fields['password2'].label='Confirm password'
        #self.fields['profile_pic'].label='Upload profile picture'
        #self.fields['profile_pic'].widget.attrs={'class':'btn btn-dark'}