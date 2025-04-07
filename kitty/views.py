from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Mascota, Mediciones
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Opcional: Iniciar sesión automáticamente después del registro
            return redirect('mascota')  # Redirige a la página principal o a donde prefieras
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')


@login_required
def mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.usuario = request.user
            mascota.save()
            return redirect('mascota_info')  # Redirige a la vista de información de mascota después de guardar
    else:
        try:
            mascota = Mascota.objects.get(usuario=request.user)
            return redirect('mascota_info')
        except Mascota.DoesNotExist:
            form = MascotaForm()

    return render(request, 'mascota.html', {'form': form})


@login_required
def mascota_view(request):
    try:
        mascota = Mascota.objects.get(usuario=request.user)
    except Mascota.DoesNotExist:
        return redirect('mascota')

    return render(request, 'mascota_info.html', {'mascota': mascota})


# 🆕 Vista para registrar medición (recibir datos desde el ESP32)
@csrf_exempt
def registrar_medicion(request):
    if request.method == 'POST':
        try:
            # Cargar los datos del cuerpo de la solicitud
            data = json.loads(request.body)

            # Obtener el usuario actual
            usuario = request.user

            # Obtener la mascota asociada al usuario, si no existe, devolver error
            try:
                mascota = Mascota.objects.get(usuario=usuario)
            except Mascota.DoesNotExist:
                return JsonResponse({'error': 'No se encontró una mascota asociada al usuario'}, status=404)

            # Crear una nueva medición en la base de datos
            medicion = Mediciones.objects.create(
                mascota=mascota,
                usuario=usuario,
                peso=data.get('weight'),
                temperatura=data.get('temperature'),
                frecuencia_cardiaca=data.get('heart_rate'),  # Asumiendo que el JSON incluye frecuencia cardíaca
                observaciones=(
                    f"Humedad: {data.get('humidity')}%, "
                    f"Luz: {data.get('light')} lux, "
                    f"Fecha: {data.get('timestamp')}"
                )
            )
            return JsonResponse({'status': 'ok'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
