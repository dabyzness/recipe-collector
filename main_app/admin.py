from django.contrib import admin
# import your models here
from .models import Recipe, Instruction, Ingredient
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Instruction)
admin.site.register(Ingredient)