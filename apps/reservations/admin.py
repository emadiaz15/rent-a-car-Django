from django.contrib import admin
from apps.reservations.models import Car, Customer, Reservation

admin.site.register(Customer)
admin.site.register(Reservation)
