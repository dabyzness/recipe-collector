from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Ingredient
from .forms import InstructionForm

# Home/Login Class Based View
class Home(LoginView):
  template_name = 'home.html'

# Recipes Class Based View
class RecipeCreate(CreateView):
  model = Recipe
  fields = ['name', 'cuisine', 'description']
  success_url = '/recipes/'
  
class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['cuisine', 'description']

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'

# Ingredients Class Based View
class IngredientCreate(CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientList(ListView):
  model = Ingredient
  
class IngredientDetail(DetailView):
  model = Ingredient

class IngredientUpdate(UpdateView):
  model = Ingredient
  fields = ['name', 'category']
  
class IngredientDelete(DeleteView):
  model = Ingredient
  success_url = '/ingredients/'

# Define the home view
# def home(request):
#   return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the recipes views
def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  ingredients_recipe_doesnt_have = Ingredient.objects.exclude(id__in = recipe.ingredients.all().values_list('id'))
  instruction_form = InstructionForm()
  return render(request, 'recipes/detail.html', {'recipe': recipe, 'instruction_form': instruction_form, 'ingredients': ingredients_recipe_doesnt_have })

def add_instruction(request, recipe_id):
  form = InstructionForm(request.POST)
  if(form.is_valid()):
    new_instruction = form.save(commit=False)
    new_instruction.recipe_id = recipe_id
    new_instruction.save()
  return redirect('recipes_detail', recipe_id=recipe_id)

def assoc_ing(request, recipe_id, ingredient_id):
  Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
  return redirect('recipes_detail', recipe_id=recipe_id)