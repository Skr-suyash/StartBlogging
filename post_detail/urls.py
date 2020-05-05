from django.urls import path, include
import post_detail.views

urlpatterns = [
    path('<slug:slug>', post_detail.views.post_detail, name="post_detail"),
]