from .estado_deposito import EstadoDeposito
from lib.mod.problema.problema import Problema
from .operador_encher import  OperadorEncher
from .operador_vazar import  OperadorVazar

class ProblemaDeposito(Problema):

    def __init__(self, ligacoes, valor_inicial, valor_final):

        #Dar append na lista de operadores os operadores Encher(2), Encher(3), Vazar(2), Vazar(3)
        operadores = [OperadorEncher(ligacoes[ligacao].valor, ligacoes[ligacao].custo) for ligacao in range(len(ligacoes))]
        operadores += [OperadorVazar(ligacoes[ligacao].valor, ligacoes[ligacao].custo) for ligacao in range(len(ligacoes))]

        super().__init__(EstadoDeposito(valor_inicial), operadores)

        self.__estado_final = EstadoDeposito(valor_final)

    def objetivo(self, estado):

        return estado == self.__estado_final
    