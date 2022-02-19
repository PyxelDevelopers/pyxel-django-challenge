from django.forms import BaseForm

from .models import Recipe


class RecipeForm(BaseForm):
    class Meta:
        model = Recipe
        fields = ['title', 'preparation_mode', 'preparation_time', 'category']
