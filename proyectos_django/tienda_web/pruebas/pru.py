from gestion_pedidos.models import Articulos

art = Articulos(nombre ='Granada de mano',tipo ='explosivo',precio =39.99)
art.save()
art2 = Articulos.objects.create(nombre ='Manzana',tipo ='fruta',precio =0.79)
art.precio = 29.95
art.save()
borra = Articulos.objects.get( id=2 )
borra.delete()