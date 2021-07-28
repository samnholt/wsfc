from django.db import models

class Match(models.Model):
    match_date = models.DateField()
    home_team = models.CharField(max_length=100)
    home_score = models.IntegerField()
    away_team = models.CharField(max_length=100)
    away_score = models.IntegerField()

    def __str__(self):
        return self.home_team + ' vs ' + self.away_team