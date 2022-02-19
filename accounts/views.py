from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
            return redirect('recipes:recipes')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return redirect('recipes:recipes')

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('recipes:recipes')


def auth_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipes:recipes')
        else:
            return redirect('recipes:recipes')


def logout_user(request):
    logout(request)
    return redirect('recipes:recipes')
