from django.contrib import admin
from gestion_pedidos.models import *
# Register your models here.

class ClientesAdmin( admin.ModelAdmin ):
    list_display = ("nombre", "direccion", "email")
    search_fields = ("nombre", "direccion")


class ArticulosAdmin( admin.ModelAdmin ):
    list_display = ("nombre", "tipo")
    search_fields = ("nombre", "tipo")
    list_filter = ("tipo",)


class PedidosAdmin( admin.ModelAdmin ):
    search_fields = ("numero",)
    list_filter = ("fecha",)
    date_hierarchy = "fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)