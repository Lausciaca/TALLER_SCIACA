from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Orden
from .forms import OrdenForm, OrdenGeneralForm

# Create your views here.
class OrdenListView(ListView):
    model = Orden

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
    

class OrdenGeneralForm(CreateView):
    def post(self, request, pk):
        orden = get_object_or_404(Orden, pk=pk)  # Buscar la orden existente
        trabajos = request.POST.getlist("tipo-trabajo")
        partes = request.POST.getlist("parte-vehiculo")

        # Si la orden ya tiene trabajos guardados, cargarlos primero
        trabajos_json = orden.trabajos_realizados or {}

        # Agregar los nuevos trabajos sin borrar los anteriores
        for i in range(len(trabajos)):
            tipo = trabajos[i]
            parte = partes[i]
            if tipo and parte:
                if tipo not in trabajos_json:
                    trabajos_json[tipo] = []
                trabajos_json[tipo].append(parte)

        # Guardar los cambios en la orden existente
        orden.trabajos_realizados = trabajos_json
        orden.save()

        return JsonResponse({"success": True, "trabajos_actualizados": trabajos_json})