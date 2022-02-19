from django.shortcuts import render

from .models import Recipe
from .forms import RecipeForm


def recipes(request):
    return render(request, 'recipes/pages/recipe_list.html')


def recipes_detail(request, recipe_id):
    # TODO Pegar informações de uma receita específica.
    pass


def recipes_create(request):
    # TODO Criar uma nova receita no banco de dados.
    pass


def recipes_update(request):
    # TODO Atualizar dados de uma receita.
    pass


def recipes_delete(request):
    # TODO Remover uma receita do banco de dados.
    pass
