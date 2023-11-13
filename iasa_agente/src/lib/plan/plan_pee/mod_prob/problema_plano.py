from mod.problema.problema import Problema
from mod.agente.estado_agente import EstadoAgente

"""
Classe ProblemaPlan:
    Classe que verifica que atinjimos o objetivo no contexto do problema, criando um trajeto com base 
    no mecanismo de procura.
"""

class ProblemaPlan(Problema):

    def __init__(self, modelo_plan, estado_final):
        #problema recebe lista estado inicial e lista de operadores
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        #definir estado final 
        self.__estado_final = estado_final


    #ver se o estado atual é o objetivo
    def objetivo(self, estado):
        return estado == self.__estado_final
