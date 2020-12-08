lista =[1,2,3,4,5,6]

print(len(lista))
del lista[2]
print(lista[2])
print(len(lista))
print("lista al reves:",end=" ")
for i in range(len(lista)-1,-1,-1):
    print(lista[i],end=", ")

print()

if type(lista) == list:
    print('es una lista valor=' + str(lista))
else:
    print('no es una lista')

lista = 'otra cosa'
if type(lista) == list:
    print('es una lista' )
else:
    print('no es una lista')