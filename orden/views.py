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
    success_url = reverse_lazy('orden:ordenes')
    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)  # Debug en consola
        return super().form_invalid(form)
