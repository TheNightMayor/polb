import datetime

from djongo import models


class Playlist(models.Model):
    Playlist_Name = models.CharField(null=True, max_length=50)
    Active = models.BooleanField(null=True, default=False)
    def __str__(self):
        return self.Playlist_Name
    
    
class Sequence(models.Model):
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
    Overlay_Asset = models.FileField(null=True, blank=True)
    class Map_Zone(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'
        F = 'F'
        G = 'G'
        H = 'H'
        S = 'S'
        T = 'T'
        NONE = 'None'
    Map_Zone = models.CharField(
        max_length=4,
        choices=Map_Zone.choices,
        default=Map_Zone.NONE
    )
    def __str__(self):
        return self.Title
    
    
# Create your models here.
