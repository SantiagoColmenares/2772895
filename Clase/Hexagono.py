from Base import Base #Importacion de la clase abstracta

class Hexagono(Base):
	def __init__(self,lado,a):
		self.lado = lado
		self.a = a
	def area(self):
		p = self.lado*6
		return (p*self.a)/2
	def perimetro(self):
		return self.lado * 6
