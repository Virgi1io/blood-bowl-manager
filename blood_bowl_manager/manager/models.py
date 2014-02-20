from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

class Race(models.Model):
    name = models.CharField(max_length=200)
    cheerleader_cost = models.IntegerField()
    assistant_coach_cost = models.IntegerField()
    reroll_cost = models.IntegerField()
    apothecary_cost = models.IntegerField()

class Team(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Player)
    race = models.ForeignKey(Race)
    treasury = models.IntegerField()
    rerolls = models.IntegerField()
    fan_factor = models.IntegerField()
    assistant_coachs = models.IntegerField()
    cheerleaders = models.IntegerField()
    apothecary = models.IntegerField()

