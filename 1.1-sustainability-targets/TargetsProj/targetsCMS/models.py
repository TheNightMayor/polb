import datetime

from djongo import models
from django.utils import timezone
from django.contrib import admin


class Playlist(models.Model):
    playlist_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.playlist_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Sequence(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    sequence_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.sequence_text
# Create your models here.
