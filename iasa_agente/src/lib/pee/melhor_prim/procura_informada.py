from abc import ABC
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim, ABC):

    def procurar(self, problema, heuristica):

        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        
        solucao = super().procurar(problema)

        return solucao