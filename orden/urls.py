from django.urls import path
from .views import OrdenCreate, OrdenListView

orden_patterns = ([
    path('', OrdenListView.as_view(), name='ordenes'),
    path('create/', OrdenCreate.as_view(), name='create'),
], 'orden')