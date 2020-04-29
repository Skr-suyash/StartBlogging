from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
class Blog(models.Model):

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=False)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):

    post = models.ForeignKey('create_blog.Blog', on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.body

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("comment_list")