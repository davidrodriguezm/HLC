from objetos.Persona import Persona
from objetos.Surfista import Surfista
from objetos.Arma import Arma

class Agente_secreto(Persona, Surfista):
    codigo_agentes = set()
    def __init__(self, nombre="Espia", edad=18, numero="12345123", tabla='blanca', codigo='007', armamento=Arma()):
        Persona.__init__(self,nombre,edad,numero)
        Surfista.__init__(self, tabla)
        self.codigo = codigo
        self.armamento = armamento

    @property
    def codigo(self):
        return self.__codigo 

    @codigo.setter
    def codigo(self, codigo):
        if codigo in Agente_secreto.codigo_agentes:
            raise ValueError('Ese codigo ya lo tiene otro agente, no se puede asignar')
        else:
            Agente_secreto.codigo_agentes.add(codigo)
            self.__codigo = codigo

    @property
    def armamento(self):
        return self.__armamento

    @armamento.setter
    def armamento(self, armamento):
        if isinstance(armamento, Arma):
            self.__armamento = armamento
        else:
            print('Eso no es un arma')  

    def disparar(self):
        self.armamento.disparar()
 
    def __str__(self):
        return '{}, {}, codigo={}, {}'.format(Persona.__str__(self), Surfista.__str__(self),\
            self.codigo, self.armamento)

    @staticmethod
    def lista_agentes():
        return Agente_secreto.codigo_agentes      
