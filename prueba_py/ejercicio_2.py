# Se intenta adivinar una contraseña con cada intento fallido se descubre un carácter

contra="loquesea"
respuesta=""
cont=0
while respuesta != contra:
    respuesta = input("introduce la contraseña. Si queres terminar responde n o N: ")
    cont+=1
    if respuesta.upper()=="N":
        break
    elif not(respuesta.upper()=="N" or respuesta==contra) and cont<len(contra):
        print("La contraseña empiezapor: ",contra[0:cont])
    elif not(respuesta.upper()=="N" or respuesta==contra) and cont>=len(contra):
        print("La contraseña empiezapor: ",contra)
else:
    print("Correcto has completado el juego")

if respuesta==contra and cont<len(contra):
    print("Lo has acertado al intento",cont)
elif respuesta==contra and cont>=len(contra):
    print("La contraseña ya se habia mostrado entera")
else:
    print("Has abandonado el juego") 
