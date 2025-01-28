from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Orden
from .forms import OrdenForm

# Create your views here.
class OrdenCreate(CreateView):
    model = Orden
    form_class = OrdenForm
