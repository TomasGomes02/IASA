from pee.melhor_prim.aval.heuristica import Heuristica
import math

"""

"""

class HeurMahn(Heuristica):

    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    def h(self, estado):
        return abs(estado.posicao[0] - self.__estado_final.posicao[0]) + abs(estado.posicao[1] - self.__estado_final.posicao[1])