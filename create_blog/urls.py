from django.urls import path
import create_blog.views

urlpatterns = [
    path('', create_blog.views.create_post, name="create_post")
]
