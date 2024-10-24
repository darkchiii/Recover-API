from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer
import os
import logging

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'text_file', 'audio_file', 'images_file', 'video_file', 'description', 'created_at', 'updated_at', 'comments', 'public', 'saves']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'comments', 'saves']

    def validate_audio_file(self, value):
        if value is None:
            return value
        valid_audio_extensions = ['.mp3', '.wav']
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in valid_audio_extensions:
            raise serializers.ValidationError('Invalid audio file extension.')
        return value

    def validate_images_file(self, value):
        if value is None:
            return value
        valid_images_extensions = ['.jpg', '.jpeg', '.png']
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in valid_images_extensions:
            raise serializers.ValidationError('Invalid images file extension.')
        return value

    def validate_video_file(self, value):
        if value is None:
            return value
        valid_video_extensions = ['.mp4', '.avi', '.mov']
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in valid_video_extensions:
            raise serializers.ValidationError('Invalid video file extension.')
        return value

    def validate(self, data):
        logging.debug("Validate method called")
        request = self.context.get('request')
        request_method = request.method if request else 'No request'
        # logging.debug(f"Request method: {request_method}")

        text_file = data.get('text_file')
        audio_file = data.get('audio_file')
        images_file = data.get('images_file')
        video_file = data.get('video_file')

        if not text_file and not audio_file and not images_file and not video_file and request_method != 'PATCH':
            raise serializers.ValidationError("You must upload at least one type of file.")

        if sum(bool(x) for x in [text_file, audio_file, images_file, video_file]) > 1:
            raise serializers.ValidationError("You can upload only one type of file in a single post.")
        return data

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post
