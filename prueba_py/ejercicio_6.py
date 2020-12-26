from objetos.Persona import Persona
from objetos.Cliente import Cliente

p1 = Persona("Ambrosio",203,"12345123")
p2 = Persona("Eufrasio",23,"87654321")
compra = ['platanos','tortilla','carne de pollo','lanzallamas 3000FX']
c1 = Cliente("Eufrasio", 23, "87654321", compra)
c2 = Cliente("Anbrosio", 34, "12345678", compra)
c3 = Cliente("Brunida", 26, "12345678", compra)
print("¿p2 y c1 son la misma persona?", p2 == c1)
setattr(c3,"dni","123") # Lo asigno mal, solo hay 3 numeros
p1.otro_atributo = True
print("nombre: {}, edad: {}, DNI: {}".format( p1.nombre, p1.edad, p1.dni) )
print("Persona", p1)
print("Cliente", c1)
print("Cliente", c2)
print("Cliente", c3)
c3.dni = "12341234"
print("Cliente", c3)
print("Persona 2 tiene otro atributo:", p1.otro_atributo)
print("Numero de clintes:", Cliente.numero())
print("Numero de clintes:", c2.numero())
del c1.nombre