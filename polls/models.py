from django.utils import timezone
from django.db import models
import  datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text + str(self.id)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta (days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #responsável por apresentar um nome legível a cada instância do obj no banco
    def __str__(self):
        return self.choice_text
