#classe que representa o problema no contexto pretendido em que existe um deposito com um determinado volume inicial 
# e um volume final, ao que vao ser aplicados varios operadores ao volume inicial ate que este chegue ao volume final
# neste problema existem dois tipos de operadores com valores diferentes, sendo eles os operadores encher e vazar

from .estado_deposito import EstadoDeposito
from lib.mod.problema.problema import Problema
from .operador_encher import  OperadorEncher
from .operador_vazar import  OperadorVazar
class ProblemaDeposito(Problema):

	def __init__(self, volume_inicial, volume_final):
		super().__init__(EstadoDeposito(volume_inicial),
						[OperadorVazar(2), OperadorVazar(3), OperadorEncher(2), OperadorEncher(3)]) #lista de operadores que caracterizam o problema

		self.__volume_final = volume_final

	#verificar se o estado atual é o objetivo do problema
	def objetivo(self, estado):
		return estado.volume == self.__volume_final