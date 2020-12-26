class Surfista():
    def __init__(self, tabla = 'negra'):
        self.tabla = tabla
       
    @property
    def tabla(self):
        return self.__tabla 

    @tabla.setter
    def tabla(self, tabla):
        self.__tabla = tabla

    def surfear(self):
        print('El sufista uso la habilidad surf para moverse por el agua')    

    def __str__(self):
        return 'tabla de surf=' + self.tabla