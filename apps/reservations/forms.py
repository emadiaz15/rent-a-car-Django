from django import forms
from apps.reservations.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['car', 'customer', 'start_date', 'end_date', 'total_price', 'status']
