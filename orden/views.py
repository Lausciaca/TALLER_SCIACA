from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Orden
from .forms import OrdenForm

# Create your views here.
class OrdenListView(ListView):
    model = Orden
    context_object_name = 'ordenes'

class OrdenCreate(CreateView):
    model = Orden
    form_class = OrdenForm
    success_url = reverse_lazy('orden:ordenes')

    def form_valid(self, form):
        form.instance.estado = 'particular_uno'
        return super().form_valid(form)
    

    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)  # Debug en consola
        return super().form_invalid(form)

class OrdenDetailView(DetailView):
    model = Orden
    context_object_name = 'orden'

    def get_object(self):
        # Modifica para que busque la orden por id
        return get_object_or_404(Orden, id=self.kwargs['id'])
    
    

class OrdenDeleteView(DeleteView):
    model = Orden
    success_url = reverse_lazy('orden:ordenes')

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.kwargs['id'])  # Buscar por 'id'
    