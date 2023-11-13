from lib.plan.plano import Plano
"""
Classe PlanoPDM:
    Classe que é utilizada, dada a utilidade e a politica, para gerar uma solucao.
"""


class PlanoPDM(Plano):

    def __init__(self, utilidade, politica):    
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado) #retorna o operador correspondente ao estado
    
    def mostrar(self, vista):
        
        if self.__politica:
            
            #se erro ou utilidade ou politica nao estao no formato correto
            vista.mostrar_valor(self.__utilidade)
            vista.mostrar_politica(self.__politica)