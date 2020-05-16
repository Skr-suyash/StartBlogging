from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Blog(models.Model):

    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    is_draft = models.BooleanField(default=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.is_draft = False
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=False)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

    
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Blog)

class Comment(models.Model):

    post = models.ForeignKey('create_blog.Blog', on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("comments", kwargs={"slug": self.post.slug})

    class Meta:
        ordering = ["-date_created"]