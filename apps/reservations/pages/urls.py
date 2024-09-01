from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('reserve/<int:car_id>/', views.reservation_create, name='reservation_create'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/', views.reservation_list, name='reservation_list'),  # Esta ruta es la que corresponde a la vista reservation_list
]
