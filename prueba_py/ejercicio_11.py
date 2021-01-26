from datetime import datetime

def operaciones(nombre):
    def decorador(funcion):
        def envoltorio(*args, **kwargs):
            fecha = datetime.now()
            print('hoy es dia {} del mes {} del año {}'.format( fecha.day, fecha.month, fecha.year ) )
            print('Se ha llamado a:', nombre)
            return funcion( *args, **kwargs)

        return envoltorio

    return decorador

@operaciones('suma')
def suma( *args, **kwargs ):
    resul = 0
    if  args : 
        for i in args:
            resul += i

    if  kwargs : 
        for v in kwargs.values():
            resul += v  

    return resul

@operaciones('multiplicar')
def multiplicar( *args, **kwargs ):
    resul = 1
    if  args : 
        for i in args:
            resul *= i

    if  kwargs : 
        for v in kwargs.values():
            resul *= v  

    return resul

lista = [5, 7, 6, 2]
mapa =  {'a': 3, 'b': 5, 'c' : 4, 'd' : 9}
print( 'Resultado:', suma( 2, 6 ) )
print( 'Resultado:', multiplicar( 3, 6, 3 ) )
print( 'Resultado:', suma( *lista ) )
print( 'Resultado:', multiplicar( **mapa ) )