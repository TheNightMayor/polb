from django.apps import AppConfig
from djongo import models

class TargetscmsConfig(AppConfig):
    id = models.BigAutoField(primary_key=True)
    name = 'targetsCMS'
