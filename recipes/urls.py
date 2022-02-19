from unicodedata import name
from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:recipe_id>/', views.recipes_detail, name="recipes_detail"),
    path('user/<int:user_id>/', views.recipes_logged_user, name="recipes_user"),
    path('category/<int:category_id>/', views.recipes_category, name="recipes_category"),  # noqa E501
]
