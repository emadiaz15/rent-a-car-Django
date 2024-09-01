from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),  # Ruta para la vista principal (home)
    path('contact/', views.contact_view, name='contact'),  # Ruta para la vista de contacto
    # Otras rutas si es necesario
]
