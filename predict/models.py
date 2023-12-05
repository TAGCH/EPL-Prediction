from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    score_team1 = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    score_team2 = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    date = models.DateField()


class Prediction(models.Model):
    match_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score_team1 = models.IntegerField()
    score_team2 = models.IntegerField()
