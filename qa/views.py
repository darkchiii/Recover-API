from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer
from django.db.models import Subquery, OuterRef, Q
from rest_framework.response import Response
from app.permissions import IsOwnerOrReadOnly

class AskQuestionView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

# Post question
    def perform_create(self, serializer):
        questioner = self.request.user
        respondent_id = self.kwargs['user_id']
        serializer.save(respondent_id=respondent_id, questioner=questioner)

# Get users questions inbox
    def get_queryset(self):
        print("get_queryset called")
        user = self.request.user
        # print(user)
        return Question.objects.filter(respondent=user).filter(answer__isnull=True)

# Post answer to question
class AnswerQuestionView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logged_in_user = self.request.user
        question_id = self.kwargs['question_id']
        print(question_id)

        try:
            question = Question.objects.get(respondent=logged_in_user, id=question_id)
            serializer.save(respondent=logged_in_user, question=question)

        except question.DoesNotExist:
            raise ValidationError("No question matches the provided query")

# Get questions that were already answered
    def get_queryset(self):
        user=self.kwargs['user_id']
        answers = Answer.objects.filter(respondent=user).select_related('question')
        return answers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for answer in queryset:
            item = {
                'question_content': answer.question.content,
                'answer_content': answer.content,
                'answered_on': answer.date,
                'asked_by': answer.question.questioner.name if not answer.question.anonymous else 'Anonymous',
                'responded_by': answer.respondent.name,
            }
            data.append(item)
        return Response(data)

# Get answer details
class AnswerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    queryset = Answer.objects.all()