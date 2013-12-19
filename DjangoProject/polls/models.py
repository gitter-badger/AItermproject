import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    #host = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    deadline_date =  models.DateTimeField('deadline to answer')
    comment = models.CharField(max_length=2000)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

class Activity(models.Model):
    poll = models.ForeignKey(Poll)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    time_duration_hours = models.IntegerField(default=1)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

class Day(models.Model):
    activity = models.ForeignKey(Activity)
    day = models.DateTimeField('day')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.day.isoformat()

class Vote(models.Model):
    user = models.ForeignKey(User)
    #activity = models.ForeignKey(Activity)
    preference_value = models.IntegerField(default=0)
    comment = models.CharField(max_length=2000)
    day = models.ForeignKey(Day)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.preference_value +"on the "+ Day.objects.get(id=self.day)




