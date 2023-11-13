#from .lib.ecr.reaccao import Reaccao
from ecr.reaccao import Reaccao
from controlo_react.reaccoes.aproximar.estimulo.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

"""Reaccao"""

class AproximarDir(Reaccao):

    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))