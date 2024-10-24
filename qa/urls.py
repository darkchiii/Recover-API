from django.urls import path
from .views import AskQuestionView, AnswerQuestionView, AnswerDetailsView

urlpatterns = [
    path('ask/<user_id>/', AskQuestionView.as_view(), name='ask-question'),
    path('ask/questions/', AskQuestionView.as_view(), name='inbox-questions'),
    path('answer/<int:question_id>/', AnswerQuestionView.as_view(), name='answer-question'),
    path('answers/<int:user_id>/', AnswerQuestionView.as_view(), name='user-answers'),
    path('answers/<int:answer_id>', AnswerDetailsView.as_view(), name='answer-details'),
]
