#Classe operador que representa a accao aplicada ao estado 
from lib.mod.operador import Operador
from abc import abstractmethod

class OperadorTransferir(Operador):
	
	def __init__(self, volume):
		self._volume = volume

	@abstractmethod
	def aplicar(self, estado):
		"""aplicar o operador ao estado"""

	#como no operador vazar o custo nao pode ser o volume devido a valores negativos,
	#utilizada a funcao abs do python, servindo assim para ambos encher e vazar
	def custo(self, estado, estado_succ):
		return abs(estado_succ.volume - estado.volume) ** 2