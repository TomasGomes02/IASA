from ecr.estimulo import Estimulo
from sae import Elemento

"""
Classe EstimuloAlvo:
    Deteta um alvo numa determinada direçao

"""

class EstimuloAlvo(Estimulo):
    """
    Recebe a direção de um estimulo que está a receber e o respetivo gama.
    O gama será um valor exponencial que ajuda a definir a intensidade dos alvos.
    Este valor varia de 0 a 1.

    """

    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama

    """
    Método detetar

    
    """

    
    
    def detectar(self, percepcao):
        elem, dist, _ = percepcao.per_dir[self.__direccao]
        return self.__gama ** dist if (elem == Elemento.ALVO) else 0