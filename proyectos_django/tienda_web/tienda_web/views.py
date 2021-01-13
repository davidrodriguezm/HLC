from django.http import HttpResponse
from django.template import Template
from django.template.loader import  get_template
from datetime import datetime

def saludo(request):
    nombre = "David"
    fecha = datetime.now()
    compra = ['Platanos','Tortilla de patatas','Carne de pollo','Lanzallamas 3000FX']
    vacia = []

    docu_ex = get_template('index.html')
    documento = docu_ex.render({"usuario":nombre, "fecha":fecha, "compra":compra, "vacia":vacia })
    return HttpResponse(documento) #http://127.0.0.1:8000/saludo/

def captura(request, edad, nombre):
    return HttpResponse('Tiene la edad de {} y se llama {}'.format(edad, nombre) ) #http://127.0.0.1:8000/captura/23/albedo