
from django.contrib import admin
from django.urls import path,include
from .views import login_blog

app_name='auth'

urlpatterns = [
    
    path('login',login_blog, name='login-blog'),
    
  ]