from django.db import models
from django.db.models.functions import Length
from django.utils.html import MAX_URL_LENGTH

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)
    instagram = models.CharField(max_length=25)
    by = models.CharField(max_length=25)
    motivo = models.CharField(max_length=100)

