class Arma():
    def __init__(self, tipo="metralleta", modelo='YG45'):
        self.tipo = tipo
        self.modelo = modelo

    @property
    def tipo(self):
        return self.__tipo 

    @tipo.setter
    def tipo(self, tipo):
       self.__tipo = tipo

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
       self.__modelo = modelo  

    def disparar(self):
        print('Piuuun piuuun')   

    def __str__(self):
       return 'Arma:{'+ 'tipo={}, modelo={}'.format(self.tipo, self.modelo) +'}'