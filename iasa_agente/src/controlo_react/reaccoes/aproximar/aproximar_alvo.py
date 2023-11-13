from ecr.prioridade import Prioridade
from sae import Direccao
from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir

""""""
class AproximarAlvo(Prioridade):

    def __init__(self):
        super().__init__([AproximarDir(direccao) for direccao in list(Direccao)])


