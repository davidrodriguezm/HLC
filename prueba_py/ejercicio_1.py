import math
# He probado varias cosas en este ejercicio
edad = int(input("Dime tu edad:"))
nombre = input("Dime tu nombre:")
if edad>=18:
    print(nombre+" tiene",edad,"es mayor de edad")
    print("tu nombre empieza por "+nombre[0]+" y termina por "+nombre[len(nombre)-1])
    raiz = round(math.sqrt(edad),2)
    print(raiz,"es la raiz cuadrad de la edad")
elif edad<0:
    print('La edad no puede ser negativa\ntu nombre invertido: ' + nombre[::-1])
else:
    print(nombre+" tiene",edad,"es menor de edad")