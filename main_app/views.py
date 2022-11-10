from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import InstructionForm

# Define the Class Views
class RecipeCreate(CreateView):
  model = Recipe
  fields = '__all__'
  success_url = '/recipes/'
  
class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['cuisine', 'description']

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'

# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the recipes views
def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  instruction_form = InstructionForm()
  return render(request, 'recipes/detail.html', {'recipe': recipe, 'instruction_form': instruction_form })

def add_instruction(request, recipe_id):
  form = InstructionForm(request.POST)
  if(form.is_valid()):
    new_instruction = form.save(commit=False)
    new_instruction.recipe_id = recipe_id
    new_instruction.save()
  return redirect('recipes_detail', recipe_id=recipe_id)