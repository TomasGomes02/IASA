from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar

from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

class EvitarObst(Hierarquia):

    def __init__(self):

        resposta = RespostaEvitar()

        super().__init__([EvitarDir(direccao, resposta) for direccao in list(Direccao)])