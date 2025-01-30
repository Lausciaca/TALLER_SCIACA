from django.urls import path
from .views import OrdenCreate, OrdenListView, OrdenDetailView, OrdenDeleteView

orden_patterns = ([
    path('', OrdenListView.as_view(), name='ordenes'),
    path('<int:id>/', OrdenDetailView.as_view(), name='detail'),
    path('<int:id>/delete', OrdenDeleteView.as_view(), name='delete'),
    path('create/', OrdenCreate.as_view(), name='create'),
], 'orden')