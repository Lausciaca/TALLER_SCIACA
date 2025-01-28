from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import Orden
from .forms import OrdenForm
from cliente.forms import ClienteForm

# Create your views here.
class OrdenListView(ListView):
    model = Orden

class OrdenCreate(TemplateView):
    template_name = 'orden/orden_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = ClienteForm(prefix='form1')
        context['form2'] = OrdenForm(prefix='form2')
        return context

    def post(self, request, *args, **kwargs):
        form1 = ClienteForm(request.POST, prefix='form1')
        form2 = OrdenForm(request.POST, prefix='form2')

        if form1.is_valid() and form2.is_valid():
            # Guardar ambos formularios
            form1.save()
            form2.save()
            return redirect('pagina_exito')  # Redirigir tras el éxito

        # Si hay errores, renderizar la página con los formularios llenos y los errores
        return self.render_to_response(self.get_context_data(form1=form1, form2=form2))
