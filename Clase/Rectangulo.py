from Base import Base #Importacion de la clase abstracta

class Rectangulo(Base):
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura
	def area(self):
		return self.base * self.altura
	def perimetro(self):
		return (self.base+self.altura)*2

