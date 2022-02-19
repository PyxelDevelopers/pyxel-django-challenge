from django.shortcuts import render

from .models import Recipe


def recipes(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipes/pages/recipe_list.html', context)


def recipes_detail(request, recipe_id):
    context = {
        'recipe': Recipe.objects.get(pk=recipe_id)
    }
    return render(request, 'recipes/pages/recipe_detail.html', context)


def recipes_category(request, category_id):
    context = {
        'recipes': Recipe.objects.filter(category__id=category_id)
    }
    return render(request, 'recipes/pages/recipe_list.html', context)


def recipes_logged_user(request, user_id):
    context = {
        'recipes': Recipe.objects.filter(user__id=user_id)
    }
    return render(request, 'recipes/pages/recipe_list.html', context)
