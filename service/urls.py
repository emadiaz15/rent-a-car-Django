from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.pages.urls')),
    path('auth/', include('apps.users.pages.urls')),
    path('cars/', include('apps.cars.pages.urls')),
    path('reservations/', include('apps.reservations.pages.urls')),  # Incluyendo las URLs de reservations
]
