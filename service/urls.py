# service/urls.py (archivo principal de urls del proyecto)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ruta para las vistas principales (core)
    path("", include("apps.core.pages.urls")),

    # Ruta para las vistas de autenticación (login y registro en pages)
    path("auth/", include("apps.users.pages.urls")),

    # Ruta para la aplicación de coches (cars)
    path('cars/', include('apps.cars.pages.urls')),
]
