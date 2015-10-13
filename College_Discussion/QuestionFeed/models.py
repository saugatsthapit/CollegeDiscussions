from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    user = models.CharField(max_length=30)
    asked_date = models.DateTimeField('asked date')
    
    
    def __str__(self):
        return self.question_text
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=500)
    user = models.CharField(max_length=30)
    answered_date = models.DateTimeField('Answered Date')
    
    def __str__(self):
        return self.answer_text
        
    