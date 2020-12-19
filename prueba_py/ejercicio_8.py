def dividir( x, y ):
    try:
        return x // y
    except ZeroDivisionError as error:
        raise ValueError( error.args )
    except Exception as error:
        raise ValueError( error.args )

try:
    dividendo = int( input("Dime un numero dividendo: ") )
    divisor = int( input("Dime un numero divisor: ") )
    resul = dividir( dividendo, divisor )
except ValueError as error:
    print(error.args)
except Exception as error:
    print(error.args)
else:
    print("El resultado de la division entera es:", resul)
finally:
    print("Terminamos el programa")