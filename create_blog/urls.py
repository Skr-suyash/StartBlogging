from django.urls import path
import create_blog.views

urlpatterns = [
    path('', create_blog.views.create_post, name="create_post"),
    path('edit/<slug:slug>/', create_blog.views.edit_post, name="edit_post"),
    path('drafts/<slug:slug>/publish', create_blog.views.publish_draft, name="publish_draft"),
]
