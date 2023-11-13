#classe que no contexto do problema representa accao de vazar o deposito
from .estado_deposito import EstadoDeposito
from .operador_transferir import  OperadorTransferir
class OperadorVazar(OperadorTransferir):
	
	def aplicar(self, estado):
		novo_volume = estado.volume - self._volume
		#se o deposito, por exemplo tiver 2 e for vazar 3, em vez de ter -1 de água terá 0
		if novo_volume < 0:
			novo_volume = 0
		return EstadoDeposito(novo_volume)

	def __repr__(self):
		return "Vazar(%s)" % self._volume
