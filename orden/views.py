from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Orden
from .forms import OrdenForm

# Create your views here.
class OrdenListView(ListView):
    model = Orden

class OrdenCreate(CreateView):
    model = Orden
    form_class = OrdenForm

