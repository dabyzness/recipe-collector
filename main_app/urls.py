from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # Recipes Routes
  path('recipes/', views.recipes_index, name='recipes_index'),
  path('recipes/<int:recipe_id>/', views.recipes_detail, name='recipes_detail'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
  path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
  path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
  path('recipes/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instruction'),
]