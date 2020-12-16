import json

def procesar_json( numero = 0 ):
    resul = None

    with open("salida-json.txt") as fichero:
        datos = json.load( fichero )
        resul = datos[ numero ]

    return resul

objeto = int( input("Dime el objeto json \n") )

print( procesar_json( objeto ) )