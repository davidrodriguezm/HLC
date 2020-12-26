def multiplicar( *args , **kwargs):
        multi = 1
        print( 'kwargs:', kwargs)
        print( 'args:', args)
        if  args : 
            for i in args:
                multi *= i

        if  kwargs : 
            for v in kwargs.values():
                multi *= v        
        
        return multi

lista = list( range( 1, 6 ) )
mapa = dict( zip( ['one', 'two', 'three', 'four', 'five'], range( 1, 6 ) ) )
print( multiplicar( *lista ) )
print( multiplicar( 1, 3, 4 ) )
print( multiplicar( **mapa ) )
print( multiplicar( tres=3, cuatro=4, seis=6 ) )
print( multiplicar( 5, 7, tres=3, cuatro=4, seis=6 ) )