from django.urls import path
from .views import user_login, user_register, profile_view

app_name = 'users'  # Asegúrate de tener este namespace

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('profile/', profile_view, name='profile'),
]
