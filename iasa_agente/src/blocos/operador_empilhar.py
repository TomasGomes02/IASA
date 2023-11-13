from copy import deepcopy
from lib.mod.operador import Operador   
from .estado_pilhas import EstadoPilhas

class OperadorEmpilhar(Operador):

    def __init__(self, origem):
        self.__origem = origem - 1

    def aplicar(self, estado):

        nova_pilha = deepcopy(estado.pilhas)
        origem_pilha = estado.pilhas[self.__origem]

        if origem_pilha:
            bloco = origem_pilha.pop(0)
            nova_pilha[0].insert(0, bloco)
            nova_pilha[self.__origem].remove(bloco)

        return EstadoPilhas(nova_pilha)

    #custo que neste contexto simboliza o indice da pilha [[ ], [ ], [ ]]                                                       1    2    3 
    def custo(self, estado, estado_succ):
        return self.__origem
    
    def __repr__(self):
        return "Empilhar(" + str(self.__origem+1) + ")"
