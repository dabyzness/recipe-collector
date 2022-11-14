from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  # Recipes Routes
  path('recipes/', views.recipes_index, name='recipes_index'),
  path('recipes/<int:recipe_id>/', views.recipes_detail, name='recipes_detail'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
  path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
  path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
  path('recipes/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instruction'),
  path('recipes/<int:recipe_id>/assoc_ing/<int:ingredient_id>/', views.assoc_ing, name='assoc_ing'),
  # Ingredients Routes
  path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
  path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
  path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
  path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
  path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
  # Signup Route
  path('accounts/signup/', views.signup, name='signup'),
]