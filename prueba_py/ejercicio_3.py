# Tabla de multiplicar de un numero y separar en giones palabras
res = int(  input("Dime un numero para ver su tabla de multiplicar: ") )
for i in range(1,11):
    print("{} x {} = {}".format(res, i, res * i))

del(res)
res = input("Dime una palabra: ")
print( "-".join(res) )
print( "La palabra repetida 5 veces: " + (res * 5) )
print( 'Las "a" se sustitullen por $: ' + res.replace("a", "$") )
print( 'Hay',res.count("e"),'"e" en la palabra' )