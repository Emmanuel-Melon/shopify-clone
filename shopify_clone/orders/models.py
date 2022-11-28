from django.db import models

# Create your models here.
from django.db import models


class Order(models.Model):
    product_name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    product_description = models.CharField(max_length=200)
      