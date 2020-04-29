from django.shortcuts import render
from .models import Blog
# Create your views here.

def create_post(request):

    if (request.method == 'POST'):
        post = Blog()
        post.author = request.user
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.body = request.POST['body']
        post.publish()

    return render(request, 'create_blog/create_post.html')