from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.backends import CustomBackend

# Create your views here.
def signup(request):

    if request.method == 'POST':
        if (request.POST['password'] == request.POST['confirm_password']):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match. Reenter.'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Not a valid username or password'})
            print('Not working')
    else:
        return render(request, 'accounts/login.html', {'error': 'Please login for Writing and Commenting privileges'})


def logout(request):
    auth.logout(request)
    return redirect('home')