# Rent a Car - Proyecto Django

## Descripción del Proyecto

Rent a Car es una aplicación web desarrollada con Django que permite a los usuarios alquilar automóviles en línea. El proyecto incluye funciones de autenticación de usuarios, gestión de automóviles, reservas y un panel de administración para gestionar el contenido.

## Características

- **Autenticación de Usuarios:** Registro, inicio de sesión y gestión de perfiles.
- **Gestión de Automóviles:** Los administradores pueden agregar, editar y eliminar automóviles.
- **Reservas:** Los usuarios pueden realizar reservas de automóviles disponibles.
- **Panel de Administración:** Un panel de administración potente y seguro.
- **Interfaz Responsiva:** Diseño adaptado a dispositivos móviles y escritorio.

## Requisitos Previos

- Python 3.10 o superior
- Django 5.1
- Virtualenv (recomendado)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tuusuario/rent-a-car.git
   cd rent-a-car
   ```

2. **Crea y activa un entorno virtual:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones:**

   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Recopila los archivos estáticos:**
   ```bash
   python manage.py collectstatic
   ```

## Ejecución del Proyecto

1. **Inicia el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

2. **Accede a la aplicación:**
   Abre tu navegador y visita `http://127.0.0.1:8000/`.

## Uso

### Autenticación de Usuarios

- Los usuarios pueden registrarse, iniciar sesión y gestionar sus perfiles.

### Gestión de Automóviles

- Los administradores pueden administrar los automóviles disponibles en el sistema.

### Realización de Reservas

- Los usuarios pueden explorar y reservar automóviles disponibles en las fechas sel
