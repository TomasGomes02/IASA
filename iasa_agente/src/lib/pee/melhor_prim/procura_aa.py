from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from .procura_informada import ProcuraInformada

"""
O método de procura A* é um método de procura completo e ótimo.
"""

class ProcuraAA(ProcuraInformada):

    def __init__(self):
        super().__init__(AvaliadorAA())