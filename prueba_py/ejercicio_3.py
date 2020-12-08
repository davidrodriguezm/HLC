# Tabla de multiplicar de un numero y separar en giones palabras

res = int(input("Dime un numero para ver su tabla de multiplicar: "))

for i in range(1,11):
    print("%d x %d = %d" % (res,i,res*i))

del(res)
res = input("Dime una palabra para separala en giones: ")

for i in res:
    print(i,end="-")
