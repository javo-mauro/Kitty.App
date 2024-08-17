from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre', 'especie', 'raza', 'fecha_nacimiento', 
            'fecha_adquisicion', 'origen', 'pasado_adoptado', 
            'tiene_enfermedades', 'enfermedades', 
            'ultima_visita_veterinario', 'tratamiento_enfermedades', 
        ]#el orden de los fils puede ser modificado para renderisar en el orden
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
            'ultima_visita_veterinario': forms.DateInput(attrs={'type': 'date'}),
            'enfermedades': forms.Textarea(attrs={'rows': 3}),
        }

