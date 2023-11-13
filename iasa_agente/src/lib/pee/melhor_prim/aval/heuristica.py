from abc import ABC, abstractmethod

class Heuristica(ABC):

    """Implementa a funcao heuristica"""
    @abstractmethod
    def h(self, estado):
        """"""