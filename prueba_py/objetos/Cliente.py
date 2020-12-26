from objetos.Persona import Persona

class Cliente(Persona):
    numero_clientes = 0
    def __init__(self,nombre="",edad=0,numero="12345678", compra=[]):
        super().__init__(nombre,edad,numero)
        self.compra = compra
        Cliente.numero_clientes += 1

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
       return ',{} compra={}'.format(super().__str__(), str(self.__compra))

    @staticmethod
    def numero():
        return Cliente.numero_clientes 
        