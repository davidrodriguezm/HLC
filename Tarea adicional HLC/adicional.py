import json

def filtrar_status( dic ): 
    
    if dic.get("status") == "running" :
        return True
    else :
        return False

def procesar_json():
    resul = None

    with open("salida-json.txt") as fichero:
        datos = json.load( fichero )
        resul = list(filter( filtrar_status, datos ))

    return resul

print( procesar_json() )