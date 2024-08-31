from django.contrib import admin
from apps.cars.models import Brand, CarModel, BodyType, Car, FeaturedCar

admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(BodyType)
admin.site.register(Car)
admin.site.register(FeaturedCar)
