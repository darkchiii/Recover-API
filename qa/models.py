from django.conf import settings
from django.db import models

class Question(models.Model):
    questioner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='q_asked')
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='q_recieved')

    anonymous = models.BooleanField(default=False)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.questioner} asked {self.respondent}"

class Answer(models.Model):
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='q_answered')
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    content = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.id}: {self.respondent} answering question {self.question.questioner}"