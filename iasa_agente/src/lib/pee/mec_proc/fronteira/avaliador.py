from abc import ABC, abstractmethod

""" Classe que avalia a prioridade""" 
class Avaliador(ABC):
    
    @abstractmethod
    def prioridade(self, no):
        """"""
