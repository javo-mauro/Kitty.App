from django.urls import path
from .views import home , mascota

urlpatterns = [
    path('',home,name='home'),
    path('mascota',mascota,name='mascota')

]