from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('register_user/', views.register, name='register'),
    path('auth/', views.auth_user, name='auth'),
    path('logout/', views.logout_user, name='logout'),
]
