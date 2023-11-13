from blocos.heur_blocos import HeurBlocos
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from lib.pee.melhor_prim.procura_custo_uniforme import ProcuraCustoUnif
from .problema_blocos import ProblemaBlocos


class PlaneadorBlocos():
    def __init__(self):
        #self.__mec_proc = ProcuraCustoUnif()
        self.__mec_proc = ProcuraAA()

    def planear(self, estado_inicial, estado_final):
        problema = ProblemaBlocos(estado_inicial, estado_final)
        #solucao = self.__mec_proc.procurar(problema)
        heur = HeurBlocos(estado_final)
        solucao = self.__mec_proc.procurar(problema, heur)

        return solucao 