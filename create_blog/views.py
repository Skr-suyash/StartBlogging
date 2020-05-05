from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
# Create your views here.


@ login_required
def create_post(request):

    if (request.method == 'POST'):
        post = Blog()
        post.author = request.user
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.body = request.POST['body']
        post.publish()
        return redirect(post.get_absolute_url())

    return render(request, 'create_blog/create_post.html')