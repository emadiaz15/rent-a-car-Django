from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from apps.reservations.models import Reservation, Customer
from apps.cars.models import Car
from django.utils import timezone
from django.db.models import Q

@login_required
def reservation_create(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        customer_id = request.POST.get('customer_id')
        customer = get_object_or_404(Customer, pk=customer_id)
        
        # Verificar disponibilidad en las fechas seleccionadas
        overlapping_reservations = Reservation.objects.filter(
            car=car,
            status='confirmed',
            start_date__lt=end_date,
            end_date__gt=start_date,
        )
        
        if overlapping_reservations.exists():
            error_message = "The car is not available for the selected dates."
            return render(request, 'reservations/reservation_form.html', {'car': car, 'customers': Customer.objects.all(), 'error_message': error_message})

        # Si no hay conflictos, crear la reserva
        reservation = Reservation.objects.create(
            customer=customer,
            car=car,
            start_date=start_date,
            end_date=end_date,
            total_price=car.price * (timezone.datetime.fromisoformat(end_date) - timezone.datetime.fromisoformat(start_date)).days,
            status='confirmed'
        )
        return redirect('reservations:reservation_detail', reservation_id=reservation.id)
    
    return render(request, 'reservations/reservation_form.html', {'car': car, 'customers': Customer.objects.all()})

@login_required
def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.all().order_by('-start_date')
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})
