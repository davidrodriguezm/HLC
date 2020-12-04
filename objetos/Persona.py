class Persona():

    def __init__(self,nombre="",edad=0,numero="12345678"):
        self.nombre = nombre
        self.edad = edad
        self.dni = numero

    @property
    def nombre(self):
        return self.__nombre 

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad 

    @edad.setter
    def edad(self,edad):
        if edad>=0:
            self.__edad = edad
        else:
            self.__edad = 0  

    @property
    def dni(self):
        return self.__dni 

    @dni.setter
    def dni(self,numero):
        if ( len( numero ) == 8 ):
            __letra = "TRWAGMYFPDXBNJZSQVHLCKE"
            self.__dni = numero + __letra[int(numero) % 23]
        else:
            self.__dni = ""   