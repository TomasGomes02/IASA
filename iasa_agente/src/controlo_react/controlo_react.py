from sae import Controlo
from ecr.comportamento import Comportamento  

"""
    Classe ControloReact:
        "Na concretização de uma arquitectura de agente, o processamento interno que relaciona 
        percepções com acções, pode ser modularizado com base num módulo de controlo.
        No caso da arquitectura de um agente reactivo, esse controlo será um controlo reactivo, em 
        que o processar das percepções é realizado com base num módulo comportamental, 
        também designado comportamento, o qual representa o comportamento geral do agente 
        que pode ser constituído por diferentes sub-comportamentos."

"""

class ControloReact(Controlo):

    """
    O construtor desta classe recebe um comportamento, que será ativado,
    por uma percepção.

    É de notar que é utilizada a notação "__" de modo a que o atributo comportamento seja privado,
    reduzindo a sua visibilidade, de acordo com os diagramas apresentados pelo docente.
    """

    def __init__(self, comportamento):
        self.__comportamento = comportamento
        

    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)

