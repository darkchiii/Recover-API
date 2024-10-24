from django.db import models
from django.conf import settings
from posts.models import Post

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        if self.parent_comment:
            return f'Reply comment with id: {self.id} made by {self.user.email} on comment with id: {self.parent_comment.id}.'
        return f'Comment with id: {self.id} made by {self.user.email} on post with id: {self.post.id}.'

class LikeComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='comments_like', on_delete=models.CASCADE)
    liked_date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.comment.id
