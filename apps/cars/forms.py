from django import forms
from .models import Brand, CarModel  # Asegúrate de importar tus modelos

class CarFilterForm(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(), 
        required=False, 
        label="Marca",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    model = forms.ModelChoiceField(
        queryset=CarModel.objects.all(), 
        required=False, 
        label="Modelo",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    body_type = forms.ChoiceField(
        choices=[('sedan', 'Sedán'), ('suv', 'SUV'), ('coupe', 'Coupé'), ('hatchback', 'Hatchback')],
        required=False, 
        label="Tipo de Carrocería",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        required=False, 
        label="Año", 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price_min = forms.DecimalField(
        required=False, 
        min_value=0, 
        label="Precio Mínimo", 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price_max = forms.DecimalField(
        required=False, 
        min_value=0, 
        label="Precio Máximo", 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    fuel_type = forms.ChoiceField(
        choices=[('gasoline', 'Gasolina'), ('diesel', 'Diésel'), ('electric', 'Eléctrico')],
        required=False, 
        label="Tipo de Combustible",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    gearbox = forms.ChoiceField(
        choices=[('manual', 'Manual'), ('automatic', 'Automático')],
        required=False, 
        label="Transmisión",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        max_length=50, 
        required=False, 
        label="Color",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
