
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Region(models.Model):
   name = models.CharField(max_length=255)
   def __str__(self):
        return self.name


class Fruits(models.Model):
    name = models.CharField(max_length=255)
    match = models.ForeignKey(Region, on_delete = models.CASCADE,  related_name="match")
    def __str__(self):
       return self.name
    
