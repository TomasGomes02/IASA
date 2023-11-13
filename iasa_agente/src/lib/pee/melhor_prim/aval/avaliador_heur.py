from abc import ABC


class AvaliadorHeur(ABC):

    def definir_heuristica(self, heuristica):
        
        self._heuristica = heuristica