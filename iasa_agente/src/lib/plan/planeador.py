from abc import ABC

#dado um conjunto de objetivos e o modelo do problema 
#produz um plano que corresponde aos passos necessarios para resolver
#o problema

#ESTADO AGENTE
#OPERADOR MOVER

class Planeador(ABC):
    
    def planear(self, modelo_plan, objectivos):
        """"""
         