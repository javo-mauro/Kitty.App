from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Mascota
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def mascota(request):
    mascota_form = MascotaForm(request.POST or None)
    return render(request, 'mascota.html', {'form': mascota_form})







#def editar_perfil(request):
#    try:
#        perfil = PerfilUsuario.objects.get(user=request.user)
#    except PerfilUsuario.DoesNotExist:
#        perfil = None

#    if request.method == 'POST':
#        form = PerfilUsuarioForm(request.POST, instance=perfil)
#        if form.is_valid():
#            perfil = form.save(commit=False)
#            perfil.user = request.user
#            perfil.save()
#            return redirect('perfil')
#    else:
#        form = PerfilUsuarioForm(instance=perfil)
#
#    return render(request, 'usuarios/editar_perfil.html', {'form': form})
