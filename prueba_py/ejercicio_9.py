def multiblos( numero, secuencia ):
    for i in secuencia:
        if i % numero == 0: yield i

intervalo = range(1, 30)
print('multiplos de 4 de 1 a 30:',end=" ")
for i in multiblos(4, intervalo): 
    print(i,end=" ")

print()
print('multiplos de 3 de 1 a 30:',end=" ")
for i in multiblos(3, intervalo): 
    print(i, end=" ")