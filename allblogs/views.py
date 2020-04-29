from django.shortcuts import render
from create_blog.models import Blog
from django.utils import timezone


def home(request):
    
    posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'allblogs/home.html', {'posts': posts})