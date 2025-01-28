from django.urls import path
from .views import OrdenCreate

orden_patterns = ([
    path('', OrdenCreate.as_view(), name='create'),
], 'orden')