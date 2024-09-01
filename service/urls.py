from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.pages.urls')),  # Rutas de la app core
    path('auth/', include('apps.users.pages.urls', namespace='users')),  # Rutas de autenticación con namespace
    path('cars/', include('apps.cars.pages.urls')),  # Rutas de la app cars
    path('reservations/', include('apps.reservations.pages.urls')),  # Incluyendo las URLs de reservations
]
