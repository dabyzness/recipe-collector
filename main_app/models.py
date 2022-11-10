from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  cuisine = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('recipes_detail', kwargs={'recipe_id': self.id})
  
class Instruction(models.Model):
  step_no = models.IntegerField()
  description = models.CharField(max_length=250)
  
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'Step {step_no}: {description}'
  
  class Meta:
    ordering = ['step_no']