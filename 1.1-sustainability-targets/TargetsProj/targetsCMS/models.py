import datetime

from djongo import models
from django.utils import timezone
from django.contrib import admin


class Playlist(models.Model):
    PlaylistName = models.CharField(max_length=50)
    Active = models.BooleanField(null=True)
    def __str__(self):
        return self.PlaylistName

class Sequence(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    # mLayoutType = models.TextChoices()
    Title = models.CharField(max_length=200)
    Statement1 = models.TextField(max_length=1000, null=True)
    Statement2 = models.TextField(max_length=1000, null=True)
    Statement3 = models.TextField(max_length=1000, null=True)
    OverlayAsset = models.CharField(max_length=100, null=True)
    StatementOfPurpose = models.TextField(max_length=1000, null=True)
    def __str__(self):
        return self.Title
    

# Create your models here.
