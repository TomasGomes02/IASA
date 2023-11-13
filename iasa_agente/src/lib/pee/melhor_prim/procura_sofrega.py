from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

"""
Classe ProcuraSofrega:
    Classe que implementa a procura informada de procura sofrega.
    É uma procura que utiliza uma heurística para a resolução do problema.

"""

class ProcuraSofrega(ProcuraInformada):

    def __init__(self):
        super().__init__(AvaliadorSof())
