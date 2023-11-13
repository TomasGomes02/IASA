
from ..mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade
from ..mec_proc.procura_grafo import ProcuraGrafo


"""Método de procura em que o critério de controlo tem a ver com uma avaliaçao do nó feita atraves de 
    uma função de avaliacao f 
    
A fronteira de exploração é ordenada por ordem crescente de f(n), ou seja, 
    os primeiros nós as expandir vão ser os melhores de acordo com esta funcão"""




class ProcuraMelhorPrim(ProcuraGrafo):

    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador

    def _manter(self, no):
        #ver se o custo do nó é inferior ao custo explorados
        return super()._manter(no) or no < self._explorados[no.estado]
    

