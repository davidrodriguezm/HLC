import random

def maxMinSum(lista):
    return ( max(lista), min(lista), sum(lista) )
# retorna una tupla de 3 valores

numeros = []

for i in range(10):
    numeros.append(random.randint(1,100))

maximo, minimo, suma = maxMinSum(numeros)
print("el maximo=",maximo,",el minimo=",minimo,", la suma= ",suma)
numeros.sort(reverse=True)
print("lista ordenada de mayor a menor:",numeros)
numeros.sort()
print("lista ordenada de menor a mayor:",numeros)
