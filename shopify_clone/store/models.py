from django.db import models

# Create your models here.
from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')