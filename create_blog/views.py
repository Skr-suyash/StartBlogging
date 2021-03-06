from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.


@ login_required
def create_post(request):

    if (request.method == 'POST'):
        if (request.POST['is_draft'] == 'False'):
            post = Blog()
            post.author = request.user
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.body = request.POST['body']
            post.publish()
            return redirect(post.get_absolute_url())

        else:
            post = Blog()
            post.author = request.user
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.body = request.POST['body']
            post.is_draft = True
            post.save()
            return redirect(post.get_absolute_url())
            # print(request.POST['title'].isspace())

    else: 
        return render(request, 'create_blog/create_post.html')

@login_required
def edit_post(request, slug):

    post = get_object_or_404(Blog, slug=slug)

    if (request.method == 'POST'):
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.body = request.POST['body']
        post.save()
        return redirect(post.get_absolute_url())
    else:
        return render(request, 'create_blog/edit_post.html', {'post': post})

@login_required
def publish_draft(request, slug):

    post = get_object_or_404(Blog, slug=slug)
    post.publish()
    return redirect('home')

