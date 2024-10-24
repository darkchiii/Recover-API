from rest_framework import serializers
from .models import Comment, LikeComment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'parent_comment', 'content', 'likes', 'created_at', 'replies']
        read_only_fields = ['id', 'user', 'post', 'likes', 'created_at', 'replies']

    # def validate(self, data):
    #     parent_comment = data.get('parent_comment')
    #     if parent_comment and parent_comment.post != data.get('post'):
    #         raise serializers.ValidationError("Parent comment must be for the same post.")
    #     return data

class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = ['id', 'user', 'comment', 'liked_date']
        read_only_fields = ['id', 'user', 'comment', 'liked_date']

    # def create(self, validated_data):
    #     like = LikeComment.objects.create(**validated_data)
    #     return like