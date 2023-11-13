
from lib.pee.mec_proc.fronteira.avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):

    def prioridade(self, no):
        #double
        return no.custo

