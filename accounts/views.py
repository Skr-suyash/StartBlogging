from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
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


## Everything about User

@ login_required
def create_profile(request):

    user = User.objects.get(username = request.user.username)

    if (request.method == 'POST'):
        response = request.POST
        user.first_name = response['first_name']
        user.last_name = response['last_name']
        user.profile.organisation = response['organisation']
        user.profile.role = response['role']
        user.profile.skills = response['skills']
        user.profile.description = response['description']
        user.save()

    return render(request, 'accounts/create_profile.html')


# View user's profile

@ login_required
def view_profile(request, user):

    user = User.objects.get(username = user)

    context = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'organisation': user.profile.organisation,
        'role': user.profile.role,
        'skills': user.profile.skills,
        'description': user.profile.description
    }
    return render(request, 'accounts/view_profile.html', {'user_profile': context})