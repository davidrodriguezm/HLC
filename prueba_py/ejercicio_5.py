import random

def maxMinSum(lista):
    return ( max(lista), min(lista), sum(lista) ) # retorna una tupla de 3 valores

lista = []
for i in range(15):
    lista.append( random.randint(1,10) )

print("lista:", lista)
maximo, minimo, suma = maxMinSum( lista )
print( "maximo = {}, el minimo = {}, la suma = {}".format( maximo, minimo, suma ) )
lista.sort(reverse=True)
print("lista ordenada de mayor a menor:", lista)
lista.sort()
print("lista ordenada de menor a mayor:",lista)
impares = [ i for i in lista if i % 2 != 0 ]
print("solo los impares:", impares)
conjunto = set( lista )
print("lista sin numeros repetidos:", conjunto)