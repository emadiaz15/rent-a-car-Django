from django.shortcuts import render, get_object_or_404
from apps.cars.models import Car
from apps.cars.forms import CarFilterForm

def car_list_view(request):
    cars = Car.objects.all()  # Obtiene todos los autos de la base de datos
    return render(request, 'cars/car_list.html', {'cars': cars})
    # Renderiza la plantilla con la lista de autos

def car_list_filter(request):
    form = CarFilterForm(request.GET or None)
    cars = Car.objects.all()

    if form.is_valid():
        if form.cleaned_data['brand']:
            cars = cars.filter(car_model__brand=form.cleaned_data['brand'])
        if form.cleaned_data['model']:
            cars = cars.filter(car_model=form.cleaned_data['model'])
        if form.cleaned_data['body_type']:
            cars = cars.filter(body_type=form.cleaned_data['body_type'])
        if form.cleaned_data['year']:
            cars = cars.filter(year=form.cleaned_data['year'])
        if form.cleaned_data['price_min']:
            cars = cars.filter(price__gte=form.cleaned_data['price_min'])
        if form.cleaned_data['price_max']:
            cars = cars.filter(price__lte=form.cleaned_data['price_max'])
        if form.cleaned_data['fuel_type']:
            cars = cars.filter(fuel_type=form.cleaned_data['fuel_type'])
        if form.cleaned_data['gearbox']:
            cars = cars.filter(gearbox=form.cleaned_data['gearbox'])
        if form.cleaned_data['color']:
            cars = cars.filter(color__icontains=form.cleaned_data['color'])

    return render(request, 'cars/car_list.html', {'form': form, 'cars': cars})

# Vista para mostrar los detalles de un auto específico
def car_detail_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)  # Obtiene un auto específico o muestra un error 404 si no existe
    return render(request, 'cars/car_detail.html', {'car': car})  # Renderiza la plantilla con los detalles del auto
