from .models import ChatMessage
from rest_framework import serializers
from user.serializers import ProfileSerializer

class MessageSerializer(serializers.ModelSerializer):
    reciever_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'user', 'sender', 'sender_profile', 'reciever', 'reciever_profile', 'message', 'is_read', 'date']
