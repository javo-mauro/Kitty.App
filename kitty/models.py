import uuid
from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    OPCIONES_ADQUISICION = [
        ('comprado', 'Comprado'),
        ('adoptado', 'Adoptado'),
    ]

    OPCIONES_PASADO = [
        ('bueno', 'Bueno'),
        ('malo', 'Malo'),
        ('calle', 'De la calle'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # Ejemplo: Perro, Gato, etc.
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_adquisicion = models.DateField()
    origen = models.CharField(max_length=10, choices=OPCIONES_ADQUISICION)
    pasado_adoptado = models.CharField(max_length=10, choices=OPCIONES_PASADO, blank=True, null=True)
    tiene_enfermedades = models.BooleanField(default=False)
    enfermedades = models.TextField(blank=True, null=True)
    ultima_visita_veterinario = models.DateField(null=True, blank=True)
    tratamiento_enfermedades = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Mediciones(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='mediciones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha en que se tomó la medición
    peso = models.FloatField(help_text="Peso en kilogramos", null=True, blank=True)
    temperatura = models.FloatField(help_text="Temperatura en °C", null=True, blank=True)
    frecuencia_cardiaca = models.IntegerField(help_text="Latidos por minuto", null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Medición de {self.mascota.nombre} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
