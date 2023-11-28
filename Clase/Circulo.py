class Circulo:
	_pi = 3.1416
	def __init__(self,radio):
		self.radio = radio
	def area(self):
		return self._pi*(self.radio**2)
	def perimetro(self):
		return 2*self._pi*self.radio
