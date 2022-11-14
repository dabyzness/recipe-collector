from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Ingredient
from .forms import InstructionForm

# Home/Login Class Based View
class Home(LoginView):
  template_name = 'home.html'

# Recipes Class Based View
class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'cuisine', 'description']
  success_url = '/recipes/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = ['cuisine', 'description']

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'

# Ingredients Class Based View
class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredient
  
class IngredientDetail(LoginRequiredMixin, DetailView):
  model = Ingredient

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  fields = ['name', 'category']
  
class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  success_url = '/ingredients/'

# Define the home view
# def home(request):
#   return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the recipes views
@login_required
def recipes_index(request):
  recipes = Recipe.objects.filter(user=request.user)
  return render(request, 'recipes/index.html', { 'recipes': recipes })

@login_required
def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  ingredients_recipe_doesnt_have = Ingredient.objects.exclude(id__in = recipe.ingredients.all().values_list('id'))
  instruction_form = InstructionForm()
  return render(request, 'recipes/detail.html', {'recipe': recipe, 'instruction_form': instruction_form, 'ingredients': ingredients_recipe_doesnt_have })

@login_required
def add_instruction(request, recipe_id):
  form = InstructionForm(request.POST)
  if(form.is_valid()):
    new_instruction = form.save(commit=False)
    new_instruction.recipe_id = recipe_id
    new_instruction.save()
  return redirect('recipes_detail', recipe_id=recipe_id)

@login_required
def assoc_ing(request, recipe_id, ingredient_id):
  Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
  return redirect('recipes_detail', recipe_id=recipe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('recipes_index')
    else:
      error_message = 'Invalid sign up - try again'
      
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
