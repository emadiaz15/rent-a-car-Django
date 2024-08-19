from django.db import models
from nanoid import generate  # Importa la función generate de la biblioteca nanoid

# Modelo para las marcas de autos
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nombre de la marca, único y con longitud máxima de 50 caracteres
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación, se establece automáticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización, se actualiza automáticamente

    def __str__(self) -> str:
        return f"{self.name}"  # Devuelve el nombre de la marca al representarla como cadena

# Modelo para los modelos de autos
class CarModel(models.Model):
    # Campo único para identificar el modelo de auto, generado automáticamente y no editable
    hash = models.CharField(max_length=10, unique=True, editable=False, default=generate)    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Relación con la marca, si se elimina la marca, se eliminan los modelos asociados
    name = models.CharField(max_length=200)  # Nombre del modelo de auto, con longitud máxima de 200 caracteres
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación, se establece automáticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización, se actualiza automáticamente

    def save(self, *args, **kwargs):
        # Si el campo hash no tiene valor (es decir, es una nueva instancia), genera un nuevo ID único
        if not self.hash:
            self.hash = generate(size=10)  # Genera un ID de 10 caracteres
        super().save(*args, **kwargs)  # Llama al método save() original para guardar la instancia

    def __str__(self) -> str:
        return f"{self.name}"  # Devuelve el nombre del modelo al representarlo como cadena

    class Meta:
        ordering = ['name']  # Ordena los modelos de autos por nombre de manera ascendente

# Modelo para los tipos de carrocería de los autos
class BodyType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nombre del tipo de carrocería, único y con longitud máxima de 50 caracteres
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación, se establece automáticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización, se actualiza automáticamente

    def __str__(self) -> str:
        return f"{self.name}"  # Devuelve el nombre del tipo de carrocería al representarlo como cadena

    class Meta:
        ordering = ['name']  # Ordena los tipos de carrocería por nombre de manera ascendente

# Modelo para representar un auto específico
class Car(models.Model):
    # Campo único para identificar el auto, generado automáticamente y no editable
    hash = models.CharField(max_length=10, unique=True, editable=False, default=generate)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)  # Relación con el modelo de auto, si se elimina el modelo, se eliminan los autos asociados
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)  # Relación con el tipo de carrocería, si se elimina, se eliminan los autos asociados
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del auto, con hasta 10 dígitos y 2 decimales
    engine_size = models.DecimalField(max_digits=10, decimal_places=1)  # Tamaño del motor, con hasta 10 dígitos y 1 decimal
    image_url = models.URLField(max_length=200)  # URL de la imagen del auto, con longitud máxima de 200 caracteres
    gearbox = models.CharField(max_length=50)  # Tipo de caja de cambios, con longitud máxima de 50 caracteres
    fuel_type = models.CharField(max_length=50)  # Tipo de combustible, con longitud máxima de 50 caracteres
    color = models.CharField(max_length=50)  # Color del auto, con longitud máxima de 50 caracteres
    year = models.PositiveIntegerField()  # Año de registro del auto
    mileage = models.PositiveIntegerField()  # Kilometraje del auto
    seats = models.PositiveIntegerField()  # Número de asientos en el auto
    doors = models.PositiveIntegerField()  # Número de puertas en el auto
    is_available = models.BooleanField(default=True)  # Indica si el auto está disponible, por defecto es True
    is_featured = models.BooleanField(default=False)  # Indica si el auto es destacado, por defecto es False
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación, se establece automáticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización, se actualiza automáticamente

    def save(self, *args, **kwargs):
        # Si el campo hash no tiene valor (es decir, es una nueva instancia), genera un nuevo ID único
        if not self.hash:
            self.hash = generate(size=10)  # Genera un ID de 10 caracteres
        super().save(*args, **kwargs)  # Llama al método save() original para guardar la instancia

    def __str__(self):
        return f"{self.car_model.name} ({self.year})"  # Devuelve el nombre del modelo y el año del auto al representarlo como cadena

    class Meta:
        indexes = [
            models.Index(fields=['car_model']),  # Índice para el campo car_model, para mejorar las consultas
            models.Index(fields=['body_type']),  # Índice para el campo body_type, para mejorar las consultas
            models.Index(fields=['price']),  # Índice para el campo price, para mejorar las consultas
            models.Index(fields=['year']),  # Índice para el campo year, para mejorar las consultas
            models.Index(fields=['is_available']),  # Índice para el campo is_available, para mejorar las consultas
            models.Index(fields=['created_at']),  # Índice para el campo created_at, para mejorar las consultas
        ]
        
# Modelo para autos destacados
class FeaturedCar(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)  # Relación uno a uno con el modelo Car, si se elimina el auto, se elimina el destacado
    featured_date = models.DateTimeField(auto_now_add=True)  # Fecha en la que el auto fue destacado, se establece automáticamente
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización del destacado, se actualiza automáticamente

    def __str__(self):
        return f"{self.car.car_model.name} ({self.car.year})"  # Devuelve el nombre del modelo y el año del auto destacado al representarlo como cadena