#classe que no contexto do problema representa accao de encher o deposito
from .estado_deposito import EstadoDeposito
from .operador_transferir import  OperadorTransferir

class OperadorEncher(OperadorTransferir):
	
	def aplicar(self, estado):
		return EstadoDeposito(estado.volume + self._volume)

	def __repr__(self):
		return "Encher(%s)" % self._volume
