from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.clientes, name='clientes'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
]