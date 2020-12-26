class Persona():
    def __init__(self,nombre="",edad=0,numero=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = numero

    def __eq__(self, otro):
        return self.dni == otro.dni
        
    @property
    def nombre(self):
        return self.__nombre 

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre
        print('Ha borrado el nombre, ahora hay una persona sin nombre')

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
       self.__dni = self.__calcula_letra( numero )

    def __calcula_letra(self, numero):
        if ( len( numero ) == 8 ):
            __letra = "TRWAGMYFPDXBNJZSQVHLCKE"
            return numero + __letra[int(numero) % 23]
        else:
            return  ""

    def __str__(self):
        return 'nombre={}, edad={}, dni={}'.format(self.nombre, self.edad,self.dni)