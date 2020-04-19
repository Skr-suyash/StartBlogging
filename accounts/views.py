from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'accounts/signup', {'error': 'Username already exists.'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('home', )

    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')