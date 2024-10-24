from rest_framework import serializers
from .models import Collection
from posts.serializers import PostSerializer

class CollectionSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Collection
        fields = ['id', 'user', 'title', 'post', 'public']
        read_only_fields = ['id', 'user']