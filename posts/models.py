from django.db import models
from django.conf import settings
from rest_framework import serializers
import os
import uuid

def post_file_path(instance, filename):
    """Generate file path for new post image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('uploads', 'posts', str(instance.id), filename)

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text_file = models.TextField(blank=True)
    audio_file = models.FileField(upload_to=post_file_path, null=True, blank=True)
    images_file = models.ImageField(upload_to=post_file_path, null=True, blank=True)
    video_file = models.FileField(upload_to=post_file_path, null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    saves = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'Post by {str(self.user.email)}'