with open("ficheros/salida.txt") as fichero:
    print("El contenido del fichero:")
    print(fichero.read())
    print("\nPrimera linea del fichero:")
    fichero.seek(0)
    print(fichero.readline())
    print("Primeros 15 caracteres:")
    fichero.seek(0)
    print(fichero.read(15))
    fichero.seek(0)
    print('\nBuscar la palabra "Oranges" en el fichero:')
    cont = 0
    for linea in fichero:
        cont += 1
        if linea.find("Oranges") >= 0:
            print('Palabra "Oranges" encontrada en la posicion {} de la linea {}'.format(linea.find("Oranges"), cont) )
            break

    else:
        print('La palabra "Oranges" no esta en el fichero')