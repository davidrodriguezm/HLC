lista = list( range( 1, 10 ) )
print( "la lista:", lista )
print( "lista al reves separada por guiones:",end=" " )
for i in range(len(lista)-1,-1,-1):
    if i != 0:
        print( lista[i],end="-" )
    else:
        print( lista[i] )

if type(lista) == list:
    print( 'es una lista, valor = ' + str(lista) )
else:
    print('no es una lista')

lista = frozenset( lista )
if type(lista) == list:
    print('es una lista')
else:
    print('no es una lista.', lista)