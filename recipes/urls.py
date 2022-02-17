from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_recipes, name='get_recipes')
]
