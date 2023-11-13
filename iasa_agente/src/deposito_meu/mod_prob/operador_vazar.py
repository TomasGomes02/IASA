
from lib.mod.operador import Operador
from .estado_deposito import EstadoDeposito

class OperadorVazar(Operador):


    def __init__(self, volume, custo):

        self.__volume = volume
       
        self.__custo = custo
    """
    
    
    """
    
    def aplicar(self, estado):

        return EstadoDeposito(estado.valor - self.__volume) if estado.valor - self.__volume > 0 else EstadoDeposito(0)

    """
    
    """
    
    def custo(self, estado, estado_suc):
        return self.__custo