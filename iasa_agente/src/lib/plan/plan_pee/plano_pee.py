from plan.plano import Plano
"""
Classe PlanoPee:
    classe que é utilizada, passando a solucao, para gerar o caminho até à solucao.
"""

class PlanoPee(Plano):

    def __init__(self, solucao):
        super().__init__()
        self.__solucao = solucao

    """
    def obter_accao(self, estado):
        #se houver uma solucao

        if self.__solucao:
            #remover da lista de solucoes
            solucao = self.__solucao.remover()
            no_seguinte = self.__solucao[0] 
            #se estados corresponderem retornar o operador
            if solucao.estado == estado:
                if no_seguinte.operador:
                    return no_seguinte.operador
    """
    def obter_accao(self, estado):
        if self.__solucao.dimensao > 1:
            if estado == self.__solucao[0].estado:
                operador = self.__solucao[1].operador
                self.__solucao.remover()
                return operador

                    
    def mostrar(self, vista):
        
        vista.mostrar_solucao(self.__solucao)
        