from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from gestion_pedidos.models import *
from gestion_pedidos.forms import *


class buscar(View): #http://127.0.0.1:8000/buscar/

    def get(self,request):
        return render(request, 'buscar.html')

    def post(self, request):
        producto = request.POST["producto"]
        if producto:
            arti = Articulos.objects.filter( nombre__icontains = producto )
            return render(request, 'resultado_buscar.html', {"articulos":arti, "articulo": producto} )
        else:
            return render(request, 'resultado_buscar.html', {"mensage": "No has introducido nada"} )


class add_cliente(View): #http://127.0.0.1:8000/add_cliente/

    def get(self, request):
        formu = Formulario_cliente()
        return render(request, 'add_cliente.html', {'formulario':formu} )
            
    def post(self, request):
        formu = Formulario_cliente()
        formu = Formulario_cliente( request.POST )
        if formu.is_valid():
            datos_form = formu.cleaned_data
            Clientes.objects.create( nombre = datos_form['nombre'], direccion = datos_form['direccion'], email = datos_form['email'], telefono = datos_form['telefono'] )
            return render(request, 'add_cliente.html', {'formulario':formu , "mensage": "Cliente agregado"} )
        else:
            return render(request, 'add_cliente.html', {'formulario':formu, "error": "Datos del formulario no validos"} )

"""
def add_cliente( request): #http://127.0.0.1:8000/add_cliente/
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
            return render(request, 'add_cliente.html', {'formulario':formu} )"""           