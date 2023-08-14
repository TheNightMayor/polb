import datetime

from djongo import models
from django.utils import timezone
from django.contrib import admin


class Route(models.Model):
    _id = models.ObjectIdField()
    Title = models.CharField(max_length=200) 
    Description = models.TextField(max_length=1000, null=True)
    Origins = models.TextChoices(
        'Origins', 'China Taiwan Vietnam South Korea Thailand'
    )
    Origin = models.CharField(
        blank=True,
        max_length=25,
        choices=Origins.choices,
        default=None
    )
    Destinations = models.TextChoices(
        'Destinations', "New_York_City Kansas_City Dallas Atlanta Chicago"
    )
    Destination = models.CharField(
        blank=True, 
        choices=Destinations.choices, 
        max_length=25, 
        default=None
    )
    def __str__(self):
        return self.Title
    
    
class Product(models.Model):
    _id = models.ObjectIdField()
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        null=True
        )
    Product_Name = models.CharField(null=True, max_length=50)
    Description = models.TextField(null=True, max_length=50)
    Media = models.FileField(null=True, blank=True)
    class Product_Type(models.TextChoices):
        CHOOSE = 'Choose One:'
        EXPORT = 'Export'
        IMPORT = 'Import'
    Product_Type = models.CharField(
        max_length=20,
        choices=Product_Type.choices,
        default=Product_Type.CHOOSE
    )
    def __str__(self):
        return self.Product_Name    
# Create your models here.
