class Hexagono:
	def __init__(self,l1,l2,l3,l4,l5,l6,a):
		self.l1 = l1
		self.l2 = l2
		self.l3 = l3
		self.l4 = l4
		self.l5 = l5
		self.l6 = l6
		self.a = a
	def area(self):
		p = self.l1+self.l2+self.l3+self.l4+self.l5+self.l6
		return (p*self.a)/2
	def perimetro(self):
		return self.l1+self.l2+self.l3+self.l4+self.l5+self.l6
