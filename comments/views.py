from rest_framework.exceptions import ValidationError, NotFound
from django.shortcuts import get_object_or_404
from .models import Comment, LikeComment
from .serializers import CommentSerializer, LikeCommentSerializer
from rest_framework import generics, permissions
from app.permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# See posts comments
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)  # _ automatyczny sufiks do pola Foreign Key - post

# Create comment / Respond to a comment
    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        parent_comment_id = self.request.data.get('parent_comment')
        parent_comment = None

        if parent_comment_id:
            parent_comment = get_object_or_404(Comment, id=parent_comment_id, post_id=post_id)

        serializer.save(user=self.request.user, post_id=post_id, parent_comment=parent_comment)

# See comment details
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    lookup_field = 'comment_id'

    def get_object(self):
        comment_id = self.kwargs.get(self.lookup_field)
        return Comment.objects.get(id=comment_id)

# Like comment
class CommentLikeView(generics.CreateAPIView):
    serializer_class = LikeCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'comment_id'

    def perform_create(self, serializer):
        user = self.request.user
        comment_id = self.kwargs.get(self.lookup_field)

        #  Check if the comment exists.
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            raise NotFound("Comment does not exist.")

        #  Check if the user has already liked the comment.
        if LikeComment.objects.filter(comment=comment, user=user).exists():
            raise ValidationError("You already liked this comment.")

        comment.likes += 1
        comment.save()
        serializer.save(user=user, comment=comment)