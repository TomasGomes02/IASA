from abc import ABC, abstractmethod

"""
Interface Estímulo

    Vai detetar intensidade das características do ambiente

"""

class Estimulo(ABC):
    """
    É usada a classe ABC(Abstract Based Class)
    
    """
    @abstractmethod
    def detectar(self, percepcao):
        """detectar"""