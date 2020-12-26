import csv
import json

try:
    lista = []
    with open("ficheros/lista.csv") as f_csv:
        contenido = csv.reader(f_csv)
        lista = list( contenido )

    with open("ficheros/datos.json","w") as f_json:
        datos = []
        for i in lista:
            mapa = dict(zip(['fecha', 'fruta', 'cantidad'], [ i[0], i[1], int( i[2] ) ] ))
            datos.append( mapa )
        json.dump(datos, f_json, sort_keys = True, indent = 4)

    with open("ficheros/salida.txt","w") as f_txt:
        for i in lista:
            if lista[ len(lista) -1 ] == i :
                f_txt.writelines("fecha: {}, fruta: {}, cantidad: {}".format( i[0], i[1], i[2]) )
            else:
                f_txt.writelines("fecha: {}, fruta: {}, cantidad: {}\n".format( i[0], i[1], i[2]) )

    with open("ficheros/salida.txt") as f_info:
        while True:
            linea = f_info.readline()
            if linea == "":
                break
            else:
                print(linea,end="")
        print()    

    with open("ficheros/resultado.csv","w") as f_resul:
            imprimir = []
            escribe = csv.writer(f_resul)
            f_resul.writelines( 'fecha, fruta, cantidad\n' )
            for i in lista:
                if lista[ len(lista) -1 ] == i :
                    f_resul.writelines( "{}, {}, {}".format( i[0], i[1], i[2] )  )
                else:
                    f_resul.writelines( "{}, {}, {}\n".format( i[0], i[1], i[2] ) )

except Exception as error:
    print(error.args)
else:
    print("El proceso de escritura y lectura se completo con exito")
