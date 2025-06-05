from django.db import models

# Create your models here.
class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    