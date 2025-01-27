from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.clientes, name='clientes'),
    path('ordenes/', views.ordenes, name='ordenes'),
]