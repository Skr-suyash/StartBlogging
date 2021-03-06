"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import allblogs.views
import accounts
import create_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', allblogs.views.home, name='home'),
    path('<str:author>/drafts', allblogs.views.drafts, name='drafts'),
    path('<str:author>/myposts', allblogs.views.myposts, name='myposts'),
    path('<str:author>/myposts/<slug:slug>/delete', allblogs.views.delete, name='delete'),
    path('accounts/', include('accounts.urls')),    
    path('create_blog/', include('create_blog.urls')),
    path('<slug:slug>/comments', allblogs.views.comments, name='comments'),
    path('post_detail/<slug:slug>', allblogs.views.post_detail, name="post_detail"),
    path('about', allblogs.views.about, name="about"),

]
