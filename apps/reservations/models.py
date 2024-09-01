from django.conf import settings
from django.db import models
from apps.cars.models import Car  # Importa el modelo Car desde la aplicación Cars

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el modelo User
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    driving_license = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'Reservation {self.id} - {self.car} for {self.customer}'

    def save(self, *args, **kwargs):
        # Calcula el precio total basado en la duración de la reserva y el precio por día del coche
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)
        # Actualiza el estado de disponibilidad del coche si la reserva está confirmada
        if self.status == 'confirmed':
            self.car.is_available = False
            self.car.save()

    def calculate_total_price(self):
        days = (self.end_date - self.start_date).days
        return self.car.price * days

    class Meta:
        ordering = ['-start_date']  # Ordena por fecha de inicio de la reserva de manera descendente
