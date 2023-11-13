from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
"""
Procura Largura

Utiliza a fronteira FIFO (first in first out), para explorar primeiro os nós mais antigos.
Nesta procura, a procura decorre explorando primeiro os nós mais antigos, ou seja, os primeiros a serem gerados.


"""

class ProcuraLargura(ProcuraGrafo):

    def __init__(self):
        super().__init__(FronteiraFIFO())