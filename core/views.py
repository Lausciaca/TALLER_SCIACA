from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'core/dashboard.html')
def clientes(request):
    return render(request, 'core/clientes.html')
def vehiculos(request):
    return render(request, 'core/vehiculos.html')
def estadisticas(request):
    return render(request, 'core/estadisticas.html')
def notificaciones(request):
    return render(request, 'core/notificaciones.html')
def ajustes(request):
    return render(request, 'core/ajustes.html')