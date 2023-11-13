from abc import ABC, abstractmethod
from ecr.comportamento import Comportamento

"""
Classe ComportComp

    Define um comportamento composto, diferente de um comportamento simples que,
    que junta mais do que um comportamento, segundo o diagrama que indica
    a utilização de uma lista com objetos deste tipo.

"""

class ComportamentoComp(Comportamento, ABC):

    """

    Construtor que recebe uma lista de comportamentos.

    Utiliza-se outra vez o "__" para indicar um atributo privado.

    """

    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    """
    Método activar():
    
        Por cada comportamento presente na lista, ativa-o, 
        consoante a percepção recebida.


    """
	

    def activar(self, percepcao):
       
        temp_accoes = []       

        for comps in self.__comportamentos:

            #caso o comportamento seja None
            if comps == None:
                continue

            temp_accao = comps.activar(percepcao)

            if temp_accao is not None:
                temp_accoes.append(temp_accao)

        if temp_accoes:
            return self.selecionar_accao(temp_accoes)
        


    @abstractmethod
    def selecionar_accao(self, accoes):
        """
        Método abstrato que vai ser usado por outras classes, nomeadamente as classes
        Hierarquia e Prioridade. 
        """    