from copy import deepcopy
from lib.mod.operador import Operador
from .estado_pilhas import EstadoPilhas

class OperadorDesempilhar(Operador):

    def __init__(self, destino):
        self.__destino = destino - 1

    def aplicar(self, estado):

        nova_pilha = deepcopy(estado.pilhas) 
        origem_pilha = estado.pilhas[0] #primeira pilha
        #se existir primeira pilha
        if origem_pilha:
            bloco = nova_pilha[0].pop(0) #[] bloco corresponde ao primeiro valor da pilha, removendo-o
            nova_pilha[self.__destino].insert(0, bloco) #inserir esse valor no destino [[1,3,2],[],[]] --> [[3,2],[1],[]] por exemplo        

        return EstadoPilhas(nova_pilha)


    #custo que neste contexto simboliza o indice da pilha [[ ], [ ], [ ]]
    #                                                       1    2    3 
    def custo(self, estado, estado_succ):
        return self.__destino
    
    
    def __repr__(self):
        return "Desempilhar(" + str(self.__destino+1) + ")"
