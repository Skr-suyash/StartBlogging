from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from create_blog.models import Blog
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

def comments(request, slug):

    

    return render(request, 'allblogs/create_comment.html')