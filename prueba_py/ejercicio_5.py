import random, statistics

def maxMinSum(lista):
    return ( max(lista), min(lista), sum(lista), statistics.mean(lista) ) # retorna una tupla de 4 valores

lista = []
for i in range(15):
    lista.append( random.randint(1,10) )

print("lista:", lista)
maximo, minimo, suma, media = maxMinSum( lista )
print( "maximo = {}, el minimo = {}, la suma = {} y la media = {:.2f}".format( maximo, minimo, suma, media ) )
lista.sort(reverse=True)
print("lista ordenada de mayor a menor:", lista)
lista.sort()
print("lista ordenada de menor a mayor:",lista)
impares = [ i for i in lista if i % 2 != 0 ]
print("solo los impares:", impares)
conjunto = set( lista )
print("lista sin numeros repetidos:", conjunto)
random.shuffle( lista )
print("lista desordenada:", lista)