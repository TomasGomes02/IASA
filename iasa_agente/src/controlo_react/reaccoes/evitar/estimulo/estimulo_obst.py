from ecr.estimulo import Estimulo

"""
Classe EstimuloObst:
    Deteta um alvo numa determinada direçao

"""

class EstimuloObst(Estimulo):
    """
    

    """

    def __init__(self, direccao, intensidade = 1.0):
        self.__direccao = direccao
        self.__intensidade = intensidade

    """
    Método detetar
    
    """

    def detectar(self, percepcao):
        
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0
    

    