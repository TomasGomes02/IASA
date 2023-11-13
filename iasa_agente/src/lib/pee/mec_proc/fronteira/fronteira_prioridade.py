

""" #Ordena por prioridade consoante o que recebe do Avaliador
    #0 --> prioridade máxima 
"""
from .fronteira import Fronteira
from lib.pee.mec_proc.no import No
""" #Estrutura de dados que tem uma sequencia ordenada respeitando um critério """

from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):

    def __init__(self, avaliador):
        super().__init__()
        self._avaliador = avaliador

    #insere nó nos nós da fronteira
    def inserir(self, no):
        #avalia a prioridade do nó/variável explicativa
        prioridade = self._avaliador.prioridade(no)
        #na lista de nós agora residem tuplos com o formato (prioridade, nó)
        heappush(self._nos, (prioridade, no))

    def remover(self):
        #variavel anonima porque nao vai ser usada
        _, no = heappop(self._nos)
        return no


