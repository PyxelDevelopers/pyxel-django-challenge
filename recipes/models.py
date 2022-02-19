from distutils.command.upload import upload
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Recipe(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    case_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Imagem de capa')  # noqa E501
    preparation_mode = models.TextField(verbose_name='Modo de preparação')
    preparation_time = models.IntegerField(verbose_name='Tempo de preparação (Em minutos)')  # noqa E501
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
