from django.urls import path, include
import post_detail.views

urlpatterns = [
    path('<int:post_id>', post_detail.views.post_detail, name="post_detail"),
]