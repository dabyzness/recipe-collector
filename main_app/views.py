from django.shortcuts import render

# Add the following import
# Add the Cat class & list and view function below the imports
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'Kinda rude.', 3),
  Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  return render(request, 'recipes/index.html', { 'cats': cats })