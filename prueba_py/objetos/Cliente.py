from objetos.Persona import Persona

class Cliente(Persona):

    def __init__(self,nombre="",edad=0,numero="12345678", compra=[]):
        super().__init__(nombre,edad,numero)
        self.compra = compra

    @property
    def compra(self):
        return self.__compra 

    @compra.setter
    def compra(self,compra):
        if type(compra) == list:
            self.__compra = compra
        else:
            self.__compra = []

    def __str__(self):
       return super().__str__() + ' compra='+ str(self.__compra)
        