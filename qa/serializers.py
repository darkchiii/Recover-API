from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'questioner', 'respondent', 'anonymous', 'content', 'date']
        read_only_fields = ['date', 'questioner', 'respondent']

class AnswerSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['id', 'respondent', 'question', 'content', 'date']
        read_only_fields = ['date', 'question', 'respondent']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.question.anonymous:
            representation['asked_by'] = 'Anonymous'
        else:
            representation['asked_by'] = instance.question.questioner
        return representation