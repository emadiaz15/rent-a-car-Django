from django.urls import path
from apps.cars.pages import views


urlpatterns = [
    path("", views.car_list_view, name="car_list"),
]