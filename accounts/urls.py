from django.urls import path
import accounts.views

urlpatterns = [
    path(r'signup', accounts.views.signup, name='signup'),
    path(r'login', accounts.views.login, name='login'),
    path(r'logout', accounts.views.logout, name='logout'),
    path('profile/create', accounts.views.create_profile, name='create_profile'),
    path('<str:user>/profile/view', accounts.views.view_profile, name='view_profile'),
]

