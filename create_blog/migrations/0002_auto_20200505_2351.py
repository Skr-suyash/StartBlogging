# Generated by Django 3.0.6 on 2020-05-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]