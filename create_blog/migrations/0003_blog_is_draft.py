# Generated by Django 3.0.6 on 2020-05-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_blog', '0002_auto_20200505_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
    ]
