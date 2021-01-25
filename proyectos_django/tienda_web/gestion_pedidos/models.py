from django.db import models

# Create your models here.

class Clientes( models.Model ):
    nombre = models.CharField( max_length = 30, verbose_name = "Nombre" )
    direccion = models.CharField( max_length = 50, verbose_name = "Dirección" )
    email = models.EmailField( blank = True, null = True, verbose_name = "Correo")
    telefono = models.CharField( max_length = 15, verbose_name = "Teléfono" )
    
    def __str__(self):
        return "Cliente: {}, dirección: {}, email: {}, telefono: {}".format(self.nombre, self.direccion, self.email, self.telefono)


class Articulos( models.Model ):
    nombre = models.CharField( max_length = 30, verbose_name = "Nombre" )
    tipo = models.CharField( max_length = 20, verbose_name = "Tipo" )
    precio = models.FloatField( verbose_name = "Precio")
    def __str__(self):
        return  "Articulo: {}, Tipo: {}, Precio: {}€".format(self.nombre, self.tipo, self.precio)


class Pedidos( models.Model ):
    numero = models.IntegerField( verbose_name = "Número" )
    fecha = models.DateField( verbose_name = "Fecha" )
    entregado = models.BooleanField( verbose_name = "Entregado" )
    def __str__(self):
        return "Número: {}, Fecha: {}, Entregado: {}".format(self.numero, self.fecha, self.entregado)
