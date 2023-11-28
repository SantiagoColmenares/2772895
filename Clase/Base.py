from abc import ABC, abstractmethod

class Base(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimetro(self):
		pass
