from turtle import color
from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
  