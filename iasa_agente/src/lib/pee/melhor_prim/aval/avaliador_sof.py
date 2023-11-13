from .avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):

    def prioridade(self, no):
        #double
        return self._heuristica.h(no.estado) #pode estar mal