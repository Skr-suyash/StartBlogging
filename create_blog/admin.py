from django.contrib import admin
from create_blog import models

# Register your models here.

admin.site.register(models.Blog)
admin.site.register(models.Comment)