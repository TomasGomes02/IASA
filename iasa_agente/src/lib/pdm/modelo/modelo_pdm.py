from abc import ABC, abstractmethod

"""
Interface ModeloPDM

"""

class ModeloPDM(ABC):

    @abstractmethod
    def S(self):
        """
        Define os estados no contexto do problema seguindo 
        o processo de decisão de markov.

        """
    @abstractmethod
    def A(self, s):
        """
        Define as accoes resultantes de estados no contexto do problema seguindo 
        o processo de decisão de markov. 

        """
    @abstractmethod
    def T(self, s, a, sn):
        """
        Define a transição entre estado e estado seguinte.

        """
    @abstractmethod
    def R(self, s, a, sn):
        """
        Define a recompensa imediata de uma transição.

        """
    @abstractmethod
    def suc(self, s, a):
        """"""
    