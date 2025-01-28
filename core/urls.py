from django.urls import path, include
from . import views
from orden.urls import orden_patterns

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('ordenes/', include(orden_patterns)),
]