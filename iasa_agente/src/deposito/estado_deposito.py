#Classe que representa o estado atual do depósito 
#estado imutável - toda a informacao que o caracteriza nao pode ser alterada pelo exterior
from lib.mod.estado import Estado

class EstadoDeposito(Estado):

	def __init__(self, volume):	
		#recorrendo a um atributo privado
		self.__volume = volume
		self.__id_valor = hash(self.__volume)

	#getter do atributo privado volume
	@property
	def volume(self):
		return self.__volume

	#identificador unico inteiro
	def id_valor(self):
		return self.__id_valor