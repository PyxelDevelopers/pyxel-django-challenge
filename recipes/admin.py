from django.contrib import admin

from .models import Recipe, Category

admin.site.register(Recipe)
admin.site.register(Category)
