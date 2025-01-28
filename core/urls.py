from django.urls import path, include
from . import views
from orden.urls import orden_patterns
from cliente.urls import cliente_patterns

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', include(cliente_patterns)),
    path('ordenes/', include(orden_patterns)),
]