from django.shortcuts import render, get_object_or_404

from apps.cars.models import Car

# Vista para mostrar la lista de autos
def car_list_view(request):
    cars = Car.objects.all()  # Obtiene todos los autos de la base de datos
    return render(request, 'cars/car_list.html', {'cars': cars})
 # Renderiza la plantilla con la lista de autos

# Vista para mostrar los detalles de un auto específico
def car_detail_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)  # Obtiene un auto específico o muestra un error 404 si no existe
    return render(request, 'cars/car_detail.html', {'car': car})  # Renderiza la plantilla con los detalles del auto
