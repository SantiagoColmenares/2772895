from Base import Base #Importacion de la clase abstracta

class Triangulo(Base):
	def __init__(self, la1, la2, la3):
		self.la1 = la1
		self.la2 = la2
		self.la3 = la3
	def area(self):
		return (self.la1*self.la2)/2
	def perimetro(self):
		return self.la1 + self.la2 + self.la3

