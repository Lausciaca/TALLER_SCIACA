from django.urls import path
from .views import ClienteListView

cliente_patterns =([
    path('', ClienteListView.as_view(), name='clientes')
], 'cliente')