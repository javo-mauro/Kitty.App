from django.contrib import admin
from .models import Mascota
from .models import Mediciones

admin.site.register(Mascota) 
admin.site.register(Mediciones)
# Register your models here.
