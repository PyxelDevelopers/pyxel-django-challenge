from django.shortcuts import render


def get_recipes(request, template_name='recipes/pages/index.html'):
    return render(request, template_name)
