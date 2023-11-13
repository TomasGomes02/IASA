
from lib.mod.problema.problema import Problema
from .estado_pilhas import EstadoPilhas
from .operador_desempilhar import OperadorDesempilhar
from .operador_empilhar import OperadorEmpilhar

class ProblemaBlocos(Problema):

    def __init__(self, estado_inicial, estado_final):
        super().__init__(EstadoPilhas(estado_inicial),
                        [OperadorDesempilhar(2), OperadorDesempilhar(3),
                        OperadorEmpilhar(2), OperadorEmpilhar(3)])

        self.__estado_final = estado_final

    def objetivo(self, estado):
        #posicoes dos blocos nas pilhas
        return estado.pilhas[0] == self.__estado_final[0]