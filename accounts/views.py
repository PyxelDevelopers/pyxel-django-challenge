from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    return render(request, 'accounts/pages/login.html')


def register_view(request):
    return render(request, 'accounts/pages/register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if not username or not email or not password:
            messages.error(request, 'Preencha todos os campos!')
            return redirect('accounts:register_view')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'Nome de usuário ou e-mail já existe!')
            return redirect('accounts:register_view')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Conta criada com sucesso! Faça login!')
        return redirect('accounts:login_view')


def auth_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipes:recipes')
        else:
            messages.error(request, 'Algo deu errado, tente novamente!')
            return redirect('accounts:login_view')


def logout_user(request):
    logout(request)
    return redirect('recipes:recipes')
