from django.apps import AppConfig
from djongo import models

class BeneficialimpactsConfig(AppConfig):
    id = models.BigAutoField(primary_key=True)
    name = 'BeneficialImpacts'
