from django.db import models
from django.contrib.auth.models import User

  

# Create your models here

class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    STATUS=(
        ('True','True'),
        ('False','Flase'),
        ('Mostly true','Mostly true'),
        ('Mostly false','Mostly false'),
    )
    questionid=models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name = "related to Question")
    answer_text= models.CharField(max_length=256,choices=STATUS)
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

# class player is extended class from class User so it is extend user database
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return self.User.username

    
class UserQuestionHistory(models.Model):
    questioner_id= models.ForeignKey(Player, on_delete=models.CASCADE, related_name = "questioner")
    respoender_id= models.ForeignKey(Player, on_delete=models.CASCADE, related_name = "respoender")

class Result(models.Model):
    answer_id= models.ForeignKey(Answer, on_delete=models.CASCADE, related_name = "Answer") 
    question_id= models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "spørsmål")
    questioner_id= models.ForeignKey(Player, on_delete=models.CASCADE, related_name = "Player_1")
    respondent_id=models.ForeignKey(Player, on_delete=models.CASCADE, related_name = "Player_2")
