from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.users.models import User
from apps.users.forms import UserProfileForm

# Vista para el login de usuarios
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {username}!")
                return redirect('core:home')  # Redirige a la página de inicio
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Información inválida.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

# Vista para el registro de nuevos usuarios
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f"Cuenta creada exitosamente para {username}!")
            return redirect('core:home')  # Redirige a la página de inicio
        else:
            messages.error(request, "Hubo un error al crear la cuenta. Verifica la información proporcionada.")
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

# Vista para mostrar y editar el perfil del usuario
@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'users/profile.html', {'form': form})
