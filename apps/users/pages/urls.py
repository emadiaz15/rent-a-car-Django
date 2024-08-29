from django.urls import path
from .views import user_login, user_register

urlpatterns = [
    # Ruta para la vista de login
    path('login/', user_login, name='login'),
    
    # Ruta para la vista de registro
    path('register/', user_register, name='register'),
]
