from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

INGREDIENT_TYPE = (('MI', 'Miscellaneous'), ('FR', 'Fruit'), ('VG', 'Vegetable'), ('SP', 'Spice'), ('HE', 'Herb'), ('DY', 'Dairy'), ('CH', 'Poultry'), ('BF', 'Beef'), ('CH', 'Cheese'), ('FU', 'Mushroom'), ('OI', 'Oil'), ('FL', 'Flour'), ('PE', 'Peanut'), ('NU', 'Tree Nut'))

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=2, choices=INGREDIENT_TYPE, default=INGREDIENT_TYPE[0][0])
  
  def __str__(self):
    return f'{self.name} is of type {self.category}'
  
  def get_absolute_url(self):
    return reverse('ingredients_detail', kwargs={'pk': self.id})

class Recipe(models.Model):
  name = models.CharField(max_length=100)
  cuisine = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  
  ingredients = models.ManyToManyField(Ingredient)
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
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
    
