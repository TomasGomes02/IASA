
from lib.pee.melhor_prim.aval.avaliador_custo_uniforme import AvaliadorCustoUnif
from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraCustoUnif(ProcuraMelhorPrim):

    def __init__(self):
        super().__init__(AvaliadorCustoUnif())     
