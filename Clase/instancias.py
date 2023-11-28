from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
#Insatancias de la clase Cuadrado
c1 = Cuadrado(8)
#c2 = Cuadrado(8)
#c3 = Cuadrado(7)
#c4 = Cuadrado(20)

#A&P Cuadrado 1
#print(c1.area())
c1.set_lado(9)
print(c1.area())

#Instancias Rectangulo

r1 = Rectangulo(12,32)

print(f"El area del rectangulo es: {r1.area()}")
print(f"El perimetro del rectangulo es:{r1.perimetro()}")
