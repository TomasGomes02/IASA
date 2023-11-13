
from lib.mod.operador import Operador
from .estado_deposito import EstadoDeposito

class OperadorEncher(Operador):


    def __init__(self, volume, custo):

        self.__volume = volume
       
        self.__custo = custo
    """
    
    
    """
    
    #Aplica o volume
    def aplicar(self, estado):

        return EstadoDeposito(estado.valor + self.__volume)

    """
    
    """
    
    def custo(self, estado, estado_suc):
        return self.__custo