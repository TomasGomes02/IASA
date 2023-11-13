from .mec_util import MecUtil

"""
Classe PDM:
    Classe que implementa os fundamentais para a realização do processo de decisão de markov.
"""

class PDM():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        #self.__gama = gama
        #self.__delta_max = delta_max
        self.__mec_util = MecUtil(modelo, gama, delta_max)

    #escolher accao que leva ao estado seguinte com a melhor utilidade
    def politica(self, U):
        S, A = self.__modelo.S, self.__modelo.A
        #relacao entre estado e accao
        pol = {}
        for s in S():
            if A(s):
                pol[s] = max(A(s), key=lambda a : self.__mec_util.util_accao(s, a, U))

        return pol
    
    
    def resolver(self):
        #U, pol = self.__mec_util.utilidade(), self.politica(U)
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol