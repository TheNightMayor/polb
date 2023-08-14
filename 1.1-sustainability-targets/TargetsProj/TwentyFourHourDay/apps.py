from django.apps import AppConfig
from djongo import models

class TwentyfourhourdayConfig(AppConfig):
    id = models.BigAutoField(primary_key=True)
    name = 'TwentyFourHourDay'
