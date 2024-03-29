from django.urls import path,re_path
from . import views

app_name='groups'

urlpatterns=[
    re_path(r'^$',views.ListGroups.as_view(),name='all'),
    re_path(r'^new/$',views.CreateGroup.as_view(),name='create'),
    path('posts/in/<slug:slug>/',views.SingleGroup.as_view(),name='single'),
    path('join/<slug:slug>/',views.JoinGroup.as_view(),name='join'),
    path('leave/<slug:slug>/',views.LeaveGroup.as_view(),name='leave'), 
]