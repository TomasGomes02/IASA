from sae import Direccao
from ecr.comportamento import Comportamento
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover


from random import choice

"""
Classe Explorar:
    Classe que, sendo um comportamento simples, permite o movimento aleatório do agente sobre o ambiente.
  
"""
class Explorar(Comportamento):

    """
    Através do método aleatorio choice, é obtida uma direção aleatória a partir de uma lista de direções.
    De seguida, perante uma direção, é chamada a funcao RespostaMover que recebe esta direção, com o objetivo de mover o agente.
    """
    def activar(self, percepcao):
        direccao = choice(list(Direccao))   
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)