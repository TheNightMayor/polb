import datetime

from djongo import models
from django.utils import timezone
from django.contrib import admin


class Playlist(models.Model):
    _id = models.ObjectIdField()
    Playlist_Name = models.CharField(null= True, max_length=50)
    Active = models.BooleanField(null=True, default=False)
    def __str__(self):
        return self.Playlist_Name

class Sequence(models.Model):
    _id = models.ObjectIdField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    class Layout_Type(models.TextChoices):
        LAYOUT_ONE = 'one'
        LAYOUT_TWO = 'two'
    Layout_Type = models.CharField(
        max_length=5,
        choices=Layout_Type.choices,
        default=Layout_Type.LAYOUT_ONE
    )
    Background_Asset = models.FileField(null=True, blank=True)
    Title = models.CharField(max_length=200)
    Statement_1 = models.TextField(max_length=1000, null=True)
    Statement_2 = models.TextField(max_length=1000, null=True)
    Statement_3 = models.TextField(max_length=1000, null=True)
    Overlay_Asset = models.FileField(null=True, blank=True)
    Statement_Of_Purpose = models.TextField(max_length=1000, null=True)
    def __str__(self):
        return self.Title
    

# Create your models here.
