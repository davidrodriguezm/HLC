from objetos.Persona import Persona
from objetos.Surfista import Surfista
from objetos.Agente_secreto import Agente_secreto
from objetos.Arma import Arma

pistolita = Arma('pistola', 'LG800')
as1 = Agente_secreto("Ambrosio",203,"12345123",'verde','009')
as1.armamento = 'banana'
as1.armamento = pistolita
print(as1.armamento)
as1.disparar()
as1.surfear()
print(as1)
as2 = Agente_secreto()
print(as2)
try:
    as3 = Agente_secreto("Ambrosio",203,"12345123",'verde','009')     
except Exception as error:
    print(error.args)
else:
    print("Se puede asignar el mismo codigo al varios agentes secretos")

print('Los agentes secretos:', Agente_secreto.lista_agentes())