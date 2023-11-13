from ecr.comport_comp import ComportamentoComp

"""
Classe Hierarquia:
    Os comportamentos estão 
    organizados numa hierarquia fixa 
    de subsunção (supressão e 
    substituição)

"""

class Hierarquia(ComportamentoComp):

    """
    Comportamentos escolhidos de acordo com a hierarquia, ou seja, a ordem de 
    em que foram guardados, ou seja, sempre o primeiro elemento da lista.
    """

    def selecionar_accao(self, accoes):
        
        if accoes is not None:

            return accoes[0]
        
        