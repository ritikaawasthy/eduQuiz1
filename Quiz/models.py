from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    id= models.AutoField(primary_key=True)
    ANS_OPTION=[('A','option1'), ('B','option2'), ('C','option3'), ('D', 'option4')]
    name=models.CharField(max_length=200, blank=False, default='')
    #quiz=models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    #picture= models.FileField(upload_to='picture/', blank=True)
    ability= models.CharField(max_length=200, blank=True)
    ans= models.CharField(max_length=6,choices=ANS_OPTION, blank=False)
    option1=models.TextField( blank=False)
    option2=models.TextField( blank=False)
    option3=models.TextField( blank=False)
    option4=models.TextField( blank=False)

class Answer(models.Model):
    id=models.AutoField(primary_key=True)
    question=models.ForeignKey(to=Question, on_delete=models.CASCADE)
    user= models.ForeignKey(to=User, on_delete= models.CASCADE)
    correct= models.BooleanField()
