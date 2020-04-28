from django.shortcuts import render, get_object_or_404
from create_blog.models import Blog

# Create your views here.

def post_detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'post_detail/post_detail.html', {'post': post})