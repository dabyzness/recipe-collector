from django.db import models

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  cuisine = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  
  def __str__(self):
    return self.name