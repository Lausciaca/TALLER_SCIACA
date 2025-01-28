from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Cliente

# Create your views here.
class ClienteListView(ListView):
    model = Cliente 
