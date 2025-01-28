from django.urls import path
from .views import ClienteListView, ClienteCreate

cliente_patterns =([
    path('/', ClienteListView.as_view(), name='clientes'),
    path('/create/', ClienteCreate.as_view(), name='create')
], 'cliente')