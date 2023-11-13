from sae import Accao
from ecr.resposta import Resposta

"""
    Classe RespostaMover:
        Classe que estende de resposta e vai permitir que o agente se mova.
        Com o auxilio do super(), instancia o construtor do método pai "Resposta",
        recebendo uma direção, e a consoante a mesma, envia uma ação.
        Estas direções podem ser: Norte, Sul, Este e Oeste.
"""

class RespostaMover(Resposta):

    def __init__(self, direccao):
        super().__init__(Accao(direccao))

    