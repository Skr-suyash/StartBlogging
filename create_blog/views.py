from django.shortcuts import render

# Create your views here.

def create_post(request):
    return render(request, 'create_blog/create_post.html')