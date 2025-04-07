from django.urls import path
from .views import home, mascota, mascota_view,register,registrar_medicion

urlpatterns = [
    path('', home, name='home'),
    path('mascota/', mascota, name='mascota'),
    path('mascota_info/', mascota_view, name='mascota_info'),
    path('mascota_edit/', mascota_view, name='edit'),
    path('register/', register, name='register'),
    path('registrar_medicion/',registrar_medicion,name='registrar_medicion'),

]