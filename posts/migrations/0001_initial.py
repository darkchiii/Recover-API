# Generated by Django 5.0.6 on 2024-06-25 11:23

import django.db.models.deletion
import posts.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_file', models.TextField(blank=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=posts.models.post_file_path)),
                ('images_file', models.ImageField(blank=True, null=True, upload_to=posts.models.post_file_path)),
                ('video_file', models.FileField(blank=True, null=True, upload_to=posts.models.post_file_path)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
