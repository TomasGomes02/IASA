from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from abc import abstractproperty
"""
Procura Profundidade

Utiliza a fronteira LIFO (last in first out), para explorar primeiro os nós mais recentes.
Nesta procura, a procura decorre explorando primeiro os nós mais recentes, ou seja, os ultimos a serem gerados.


"""
class ProcuraProfundidade(MecanismoProcura):

    @property
    def complexidade_espacial(self):
        return self.__complexidade_espacial

    def __init__(self):
        super().__init__(FronteiraLIFO())
        self.__complexidade_espacial = 0

    def _memorizar(self, no):

        self._fronteira.inserir(no)

        #complexidade espacial - máximo de nós mantidos em memória
        #verifica se a nova complexidade é maior que a antiga e caso seja, substitui-a
        self.__complexidade_espacial = max(self._fronteira.dim, self.__complexidade_espacial)

