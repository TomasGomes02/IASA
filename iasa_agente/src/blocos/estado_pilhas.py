
from lib.mod.estado import Estado


class EstadoPilhas(Estado):


    def __init__(self, pilhas):
        self.__pilhas = pilhas #lista de listas
        self.__id_valor = hash(tuple(tuple(element) for element in self.__pilhas))

    
    def id_valor(self):
        return self.__id_valor
    
    @property
    def pilhas(self):
        return self.__pilhas    
    

