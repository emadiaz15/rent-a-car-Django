import json
import random
from apps.cars.models import Car, CarModel, Brand, BodyType

def run():
    # Cargar el archivo JSON
    with open('vehicles.json', 'r') as file:
        data = json.load(file)
    
    # Obtener todas las marcas y tipos de carrocería existentes en la base de datos
    brands = list(Brand.objects.all())
    body_types = list(BodyType.objects.all())

    for vehicle in data['vehicles']:
        try:
            # Seleccionar una marca y un tipo de carrocería aleatoriamente
            brand = random.choice(brands)
            body_type = random.choice(body_types)

            # Obtener o crear el modelo de auto
            car_model, created = CarModel.objects.get_or_create(
                name=vehicle['name'],
                brand=brand
            )

            # Crear el auto
            car, created = Car.objects.get_or_create(
                car_model=car_model,
                body_type=body_type,
                price=vehicle['price'],
                engine_size=float(vehicle['engine_size'].replace('L', '')),
                image_url=vehicle['image_url'],  # Usar la URL completa o relativa según tu configuración
                gearbox=vehicle['gearbox'],
                fuel_type=vehicle['fuel_type'],
                color=vehicle['color'],
                year=vehicle['year'],
                mileage=int(vehicle['mileage']),
                seats=vehicle['seats'],
                doors=vehicle['doors'],
                is_available=vehicle['is_available'],
                is_featured=vehicle['is_featured'],
                created_at=vehicle['created_at'],
                updated_at=vehicle['updated_at']
            )

            if created:
                print(f"Car created: {car}")
            else:
                print(f"Car already exists: {car}")

        except CarModel.DoesNotExist:
            print(f"Error: Car model '{vehicle['name']}' does not exist.")
        except BodyType.DoesNotExist:
            print(f"Error: Body type '{vehicle['body_type']}' does not exist.")
