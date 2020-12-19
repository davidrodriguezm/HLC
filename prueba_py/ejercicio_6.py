from objetos.Persona import Persona
from objetos.Cliente import Cliente

p1 = Persona("Ambrosio",203,"12345123")
compra = ['platanos','tortilla','carne de pollo','lanzallamas 3000FX']
c = Cliente("Eufrasio",23,"87654321",compra)
print("nombre: {}, edad: {}, DNI: {}".format( p1.nombre, p1.edad, p1.dni) )
print("Persona", p1)
print("Cliente", c)