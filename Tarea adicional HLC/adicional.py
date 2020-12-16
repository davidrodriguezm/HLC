import json

def filtrar_status( dic ):  
    if dic.get("status") == "running" :
        return True
    else :
        return False

def devolver_mapas( dic ): 
    resul = {}
    resul["name"] = dic.get("name")
    resul["cpu"] = dic.get("cpu")
    resul["mem"] = dic.get("mem")
    return resul  

def procesar_json():
    resul = None
    with open("salida-json.txt") as fichero:
        datos = json.load( fichero )
        filtrado = list(filter( filtrar_status, datos ))
        resul = list(map(devolver_mapas, filtrado))
        resul.sort( key=lambda elem: elem["cpu"], reverse=True)   
    return resul

lista = procesar_json()
suma = 0
print("Diccionarios ordenados por orden descendente de cpu:")
for i in lista:
    suma += i.get("mem")
    print(i)
else:
    print("\nLa suma de todos los mem:",suma)