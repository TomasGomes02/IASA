from abc import ABC, abstractmethod

"""
Operador:
    Aplica-se a estados, gerando novos estados e define também o custo de transição entre estados

"""

class Operador(ABC):

    @abstractmethod
    def aplicar(self, estado):
        """"""
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """"""