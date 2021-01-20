from django.db import models

# Create your models here.

class Clientes( models.Model ):
    nombre = models.CharField( max_length = 30 )
    direccion = models.CharField( max_length = 50 )
    email = models.EmailField()
    telefono = models.CharField( max_length = 15 )


class Articulos( models.Model ):
    nombre = models.CharField( max_length = 30 )
    tipo = models.CharField( max_length = 20 )
    precio = models.FloatField()


class Pedidos( models.Model ):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()