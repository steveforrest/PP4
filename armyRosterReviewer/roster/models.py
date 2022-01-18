from django.db import models

# Create your models here.
class RosterList(models.Model):
    name = models.CharField('Name Of List', max_length=50, null=False, blank=False)
    points = models.CharField('Points', max_length=4, null=False, blank=False)
    faction = models.CharField('Faction', max_length=50, null=False, blank=False)
    roster = models.TextField('Roster', null=False, blank=False)
    createdBy = models.CharField('Created By', max_length=50, null=False, blank=False)
    createdOn = models.DateField('Created On', null=False, blank=False)
    numberOfComments = models.CharField('Number Of Comments', max_length=50, null=False, blank=False)
    numberOfLikes = models.CharField('Number Of Likes', max_length=50, null=False, blank=False)
    numberOfDislikes = models.CharField('Number Of Dislikes', max_length=50, null=False, blank=False)
