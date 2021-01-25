from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import *
from gestion_pedidos.forms import *
# Create your views here.

def buscar(request): #http://127.0.0.1:8000/buscar/
    if request.method == "POST":
        producto = request.POST["producto"]
        if producto:
            arti = Articulos.objects.filter( nombre__icontains = producto )
            return render(request, 'resultado_buscar.html', {"articulos":arti, "articulo": producto} )

        else:
            return render(request, 'resultado_buscar.html', {"mensage": "No has introducido nada"} )
    else:
        return render(request, 'buscar.html')

def add_cliente(request): #http://127.0.0.1:8000/add_cliente/
    formu = Formulario_cliente()
    if request.method == "POST":
        formu = Formulario_cliente( request.POST )
        if formu.is_valid():
            datos_form = formu.cleaned_data
            Clientes.objects.create( nombre = datos_form['nombre'], direccion = datos_form['direccion'], email = datos_form['email'], telefono = datos_form['telefono'] )
            return render(request, 'add_cliente.html', {'formulario':formu , "mensage": "Cliente agregado"} )

        else:
            return render(request, 'add_cliente.html', {'formulario':formu, "error": "Datos del formulario no validos"} )
    else:
        return render(request, 'add_cliente.html', {'formulario':formu} )