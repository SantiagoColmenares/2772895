class Cuadrado:

	def __init__(self, _lado):
		self._lado = _lado

	def area(self):
		return self._lado*self._lado

	def perimetro(self):
		return self._lado*4

	def get_lado(self):
		return self._lado

	def set_lado(self, nuevo_lado):
		self._lado = nuevo_lado
