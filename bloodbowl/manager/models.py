from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=30)
    cheerleader_cost = models.IntegerField()
    assistant_coach_cost = models.IntegerField()
    reroll_cost = models.IntegerField()
    apothecary_cost = models.IntegerField()
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Coach)
    race = models.ForeignKey(Race)
    treasury = models.IntegerField()
    rerolls = models.IntegerField()
    fan_factor = models.IntegerField()
    assistant_coachs = models.IntegerField()
    cheerleaders = models.IntegerField()
    apothecary = models.IntegerField()
    def __unicode__(self):
        return self.name

class PlayerStats(models.Model):
    MA = models.IntegerField('Movement Allowance')
    ST = models.IntegerField('Strength')
    AG = models.IntegerField('Agility')
    AV = models.IntegerField('Armor Value')

class SkillCategory(models.Model):
    title = models.CharField(max_length=30)
    initial = models.CharField(max_length=1)
    def __unicode__(self):
        return self.title 

class Skill(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(SkillCategory)
    description = models.TextField()
    def __unicode__(self):
        return self.title

class PlayerSkills(models.Model):
    skills = models.ManyToManyField(Skill, related_name='+')
    new = models.ManyToManyField(SkillCategory, related_name='new+')
    double = models.ManyToManyField(SkillCategory, related_name='double+')

class PlayerType(models.Model):
    title = models.CharField(max_length=30)
    race = models.ForeignKey(Race)
    initial_stats = models.ForeignKey(PlayerStats)
    initial_skills = models.ForeignKey(PlayerSkills)
    max_count = models.IntegerField()
    cost = models.IntegerField()
    def __unicode__(self):
        return self.title

class Player(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(PlayerType)
    stats = models.ForeignKey(PlayerStats)
    skills = models.ForeignKey(PlayerSkills)
    value = models.IntegerField()
    def __unicode__(self):
        return self.name
