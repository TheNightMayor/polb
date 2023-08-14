from django.db import models

# Create your models here.

import datetime

from djongo import models
from django.utils import timezone
from django.contrib import admin


class Content(models.Model):
    _id = models.ObjectIdField()
    Title = models.CharField(max_length=100)
    Attract = models.CharField(max_length=100)
    topics = models.ManyToManyField('self')
    def __str__(self):
        return self.Title
    
class Story(models.Model):
    _id = models.ObjectIdField()
    Headline = models.CharField(max_length=50)
    Overview = models.TextField(max_length=1000, null=True)
    Media = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.Headline    
    
class Topic(models.Model):
    _id = models.ObjectIdField()
    Title = models.CharField(max_length=50)
    stories = models.ManyToManyField(Story)
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.Title



# Create your models here.
