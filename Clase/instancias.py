from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Circulo import Circulo
from Triangulo import Triangulo
#Insatancias de la clase Cuadrado
c1 = Cuadrado(8)


#A&P Cuadrado 1

c1.set_lado(9)
print(c1.area())

#Instancias Rectangulo

r1 = Rectangulo(12,32)

print(f"El area del rectangulo es: {r1.area()}")
print(f"El perimetro del rectangulo es:{r1.perimetro()}")

#Instancias Circulo
ci1 = Circulo(9)

print(f"El area del circulo es: {ci1.area()}")
print(f"El perimetro del circulo es: {ci1.perimetro()}")

#Instancias Triangulo

t1 = Triangulo(6,6,6)

print(f"El area del triangulo es: {t1.area()} \nEl perimetro del triangulo es: {t1.perimetro()}")








