from datetime import datetime

def operaciones(nombre):
    def decorador(funcion):
        def envoltorio(*args, **kwargs):
            fecha = datetime.now()
            print('hoy es dia {} del mes {} del año {}'.format( fecha.day, fecha.month, fecha.year ) )
            print('Se ha llamado a:', nombre)
            return funcion(*args, **kwargs)

        return envoltorio

    return decorador

@operaciones('suma')
def suma( a, b, c = 0, d = 0 ):
    return a + b + c + d

@operaciones('multiplicar')
def multiplicar( a, b, c = 1, d = 1 ):
    return a * b * c * d

lista = [5, 7, 6, 2]
mapa =  {'a': 3, 'b': 5, 'c' : 4, 'd' : 9}
print( suma( 2, 6 ) )
print( multiplicar( 3, 6, 3 ) )
print( suma( *lista ) )
print( multiplicar( **mapa ) )