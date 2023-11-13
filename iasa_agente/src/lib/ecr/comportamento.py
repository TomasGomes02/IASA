from abc import ABC, abstractmethod

"""
Interface Comportamento
    Irá ser implementada pelas classes Reaccao e Comportamento, 
    como indicado no diagrama.
"""

class Comportamento(ABC):

    @abstractmethod
    def activar(self, percepcao):
        """Ativar comportamento"""