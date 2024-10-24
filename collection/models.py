"""
Collection models.
"""
from django.db import models
from django.conf import settings
from posts.models import Post

class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.ManyToManyField(Post, related_name='collections')
    public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"