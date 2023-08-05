from django.apps import AppConfig
from djongo import models


class ProductsandaccessConfig(AppConfig):
    id = models.BigAutoField(primary_key=True)
    name = 'ProductsAndAccess'
