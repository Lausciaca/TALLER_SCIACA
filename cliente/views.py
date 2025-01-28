from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
class ClienteListView(ListView):
    model = Cliente 

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:clientes')

