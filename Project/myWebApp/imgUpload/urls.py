from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import home, imageprocess
from . import views

urlpatterns = [
    path(r'', views.home , name='home'),
    path(r'imageprocess' , views.imageprocess , name='imageprocess'),
    
    #path('blog', views.blog , name = 'blog'),
   
]
