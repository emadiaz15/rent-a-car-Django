from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("apps.core.pages.urls")),
    
    path('cars/', include('apps.cars.pages.urls')),
]
