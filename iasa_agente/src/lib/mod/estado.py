from abc import ABC, abstractmethod

"""
Estado:
    Identificação única por valor (em função da informação de estado)


"""

class Estado(ABC):

    #Método abstrato
    @abstractmethod
    def id_valor(self):
        """"""
    
    #Define identificação única de um objecto
    def __hash__(self):
        return self.id_valor()
    

    #Define relação de igualdade consistente com definição de identificação
    #Comparar hashes entre self e outro objeto que recebe (Estados)
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
        
        
