from lib.plan.plan_pdm.plano_pdm import PlanoPDM
from lib.pdm.pdm import PDM
from lib.plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from lib.plan.planeador import Planeador

"""
Classe PlaneadorPDM:
    Classe que gera um plano para a resolução do problema, seguindo 
    o Processo de Decisão de Markov.
"""


class PlaneadorPDM(Planeador):

    #Construtor que recebe os parametros Gama e Δ (Delta)
    def __init__(self, gama=0.85, delta_max=1.0):
        self.__gama = gama
        self.__delta_max = delta_max

    #Método que recebe o modelo do plano e os objetivos e gera um plano.
    def planear(self, modelo_plan, objectivos):
        
        problema = ModeloPDMPlan(modelo_plan, objectivos)

        U, p = PDM(problema, self.__gama, self.__delta_max).resolver()

        return PlanoPDM(U, p) 