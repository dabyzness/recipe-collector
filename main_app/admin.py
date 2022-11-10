from django.contrib import admin
# import your models here
from .models import Recipe, Instruction
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Instruction)