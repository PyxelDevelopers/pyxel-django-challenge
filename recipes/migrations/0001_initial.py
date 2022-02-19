# Generated by Django 4.0.2 on 2022-02-19 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('case_image', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Imagem de capa')),
                ('preparation_mode', models.TextField(verbose_name='Modo de preparação')),
                ('preparation_time', models.IntegerField(verbose_name='Tempo de preparação (Em minutos)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.category')),
            ],
        ),
    ]
