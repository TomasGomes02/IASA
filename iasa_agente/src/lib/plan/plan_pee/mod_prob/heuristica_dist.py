from pee.melhor_prim.aval.heuristica import Heuristica
import math

"""
Classe Heuristica Distância:
    Implementa a interface "Heuristica".
    Utilizando a distância, representa uma estimativa do custo do percurso até ao estado final.

"""


class HeurDist(Heuristica):

    #Recebe o estado final do problema que vai ser utilizado para calcular as distências.
    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    #Retorna uma estimativa do custo. A avaliação é baseada na distância até à posição do estado final.
    def h(self, estado):
        return math.dist(self.__estado_final.posicao, estado.posicao)