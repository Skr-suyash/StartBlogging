from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required
from create_blog.models import Blog, Comment
from django.utils import timezone


def home(request):
    
    posts = Blog.objects.filter(is_draft=False).filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'allblogs/home.html', {'page_obj': page_obj})


def drafts(request, author):

    drafts = Blog.objects.filter(author__id=request.user.id).filter(is_draft=True).filter(date_created__lte=timezone.now()).order_by('-date_created')

    print("User is : " + str(type(request.user)))

    return render(request, 'allblogs/drafts.html', {'drafts': drafts})


def myposts(request, author):

    myposts = Blog.objects.filter(author__id=request.user.id).filter(is_draft=False).filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'allblogs/myposts.html', {'myposts': myposts})


def delete(request, author, slug):

    post_to_be_deleted = get_object_or_404(Blog,slug=slug)
    post_to_be_deleted.delete()
    return redirect('home')


### For Comments

@ login_required
def comments(request, slug):

    post = get_object_or_404(Blog, slug=slug)
    comments = []

    try:
        comments = get_list_or_404(Comment, post=post)
    except Http404:
        error = "No comments yet"
        print(error)


    if (request.method == 'POST'):
        print(request.POST)
        comment = Comment()
        comment.post = post
        comment.author = request.user
        comment.body = request.POST['comment_body']
        print(request.POST['comment_body'])
        comment.date_created = timezone.now()
        comment.save()
        return redirect('comments', slug=post.slug)
    
    return render(request, 'allblogs/create_comment.html', {'post': post, 'comments':comments})

