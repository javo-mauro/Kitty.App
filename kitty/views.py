from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Mascota
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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
            # Intentar obtener la mascota existente del usuario
            mascota = Mascota.objects.get(usuario=request.user)
            return redirect('mascota_info')  # Redirige a la vista de información si ya existe una mascota
        except Mascota.DoesNotExist:
            form = MascotaForm()  # Formulario vacío para usuarios nuevos

    return render(request, 'mascota.html', {'form': form})

@login_required
def mascota_view(request):
    try:
        mascota = Mascota.objects.get(usuario=request.user)
    except Mascota.DoesNotExist:
        return redirect('mascota')  # Redirige al formulario si no hay mascota registrada

    return render(request, 'mascota_info.html', {'mascota': mascota})