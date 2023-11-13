
from plan.plan_pee.mod_prob.heuristica_manh import HeurMahn
from plan.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.problema_plano import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPee
from plan.plan_pee.mod_prob.heuristica_dist import HeurDist


"""
Classe PleanadorPee:
    Classe que implementa um planeador baseado na procura em espaços de estados.
    Implementa a interface de "Planeador"

"""


class PlaneadorPee(Planeador):

    def __init__(self):
        super().__init__()
        self.__mec_proc = ProcuraAA()
        self.__heuristica = None

    def planear(self, modelo_plan, objectivos):
        
        prob = ProblemaPlan(modelo_plan, objectivos[0])

        #heur = HeurDist(objectivos[0])
        #heur = HeurMahn(objectivos[0])
        heur = self.__heuristica(objectivos[0])

        solucao = PlanoPee(self.__mec_proc.procurar(prob, heur))

        self.__mostrar()

        return solucao
    
    def set_heuristica(self, tipo):
        if tipo == "Distancia":
            self.__heuristica = HeurDist
        elif tipo == "Manhatam":
            self.__heuristica = HeurMahn

    def __mostrar(self):
        if self.__heuristica == HeurDist:
            print("Heuristica Distancia")
        elif self.__heuristica == HeurMahn:
            print("Heuristica Manhatam")
        print("Complexidade Temporal ", self.__mec_proc.complexidade_temporal)
        print("Complexidade Espacial ", self.__mec_proc.complexidade_espacial)