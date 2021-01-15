from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    nombre = "David"
    fecha = datetime.now()
    compra = ['Platanos','Tortilla de patatas','Carne de pollo','Lanzallamas 3000FX']
    vacia = []
    dic = {"usuario":nombre, "fecha":fecha, "compra":compra, "vacia":vacia }
    return render(request, 'saludo.html', dic) #http://127.0.0.1:8000/saludo/

def captura(request, edad, nombre):
    return HttpResponse('Tiene la edad de {} y se llama {}'.format(edad, nombre) ) #http://127.0.0.1:8000/captura/23/albedo