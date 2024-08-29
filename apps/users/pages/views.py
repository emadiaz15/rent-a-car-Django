from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# Vista para el login de usuarios
def user_login(request):
    # Si la petición es POST, significa que el usuario está intentando iniciar sesión
    if request.method == 'POST':
        # Crear un formulario de autenticación con los datos enviados
        form = AuthenticationForm(request, data=request.POST)
        
        # Validar el formulario
        if form.is_valid():
            # Si el formulario es válido, se obtienen el nombre de usuario y la contraseña
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Intentar autenticar al usuario
            user = authenticate(username=username, password=password)
            
            # Si la autenticación es exitosa, iniciar la sesión
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {username}!")
                # Redirigir al usuario a la página de inicio o a otra página
                return redirect('home')
            else:
                # Si la autenticación falla, mostrar un mensaje de error
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            # Si el formulario no es válido, mostrar un mensaje de error
            messages.error(request, "Información inválida.")
    
    # Si la petición es GET, se muestra el formulario de login vacío
    else:
        form = AuthenticationForm()
    
    # Renderizar la plantilla de login con el formulario
    return render(request, 'pages/login.html', {'form': form})

# Vista para el registro de nuevos usuarios
def user_register(request):
    # Si la petición es POST, significa que el usuario está intentando registrarse
    if request.method == 'POST':
        # Crear un formulario de creación de usuario con los datos enviados
        form = UserCreationForm(request.POST)
        
        # Validar el formulario
        if form.is_valid():
            # Si el formulario es válido, se guarda el nuevo usuario
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            messages.success(request, f"Cuenta creada exitosamente para {username}!")
            # Redirigir al usuario a la página de inicio o a otra página
            return redirect('home')
        else:
            # Si el formulario no es válido, mostrar un mensaje de error
            messages.error(request, "Hubo un error al crear la cuenta. Verifica la información proporcionada.")
    
    # Si la petición es GET, se muestra el formulario de registro vacío
    else:
        form = UserCreationForm()
    
    # Renderizar la plantilla de registro con el formulario
    return render(request, 'pages/register.html', {'form': form})

# Nota: Asegúrate de tener una vista "home" configurada o cambia "redirect('home')" a la ruta que prefieras.
