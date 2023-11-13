"""
Classe Resposta

    Classe que vai servir para gerar a ação do agente.


"""

class Resposta:

    """
    Construtor da classe Resposta, recebe uma accao.

    Neste caso, seguindo o diagrama, utiliza-se "_" para declarar
    a variável como protected.
    
    """

    def __init__(self, accao):
        self._accao = accao

    """
    Método activar():
        Recebe como argumentos uma percepcao e a intensidade, 
        gerando uma ação e retornando-a
    
    """

    def activar(self, percepcao, intensidade=0):
        self._accao.prioridade = intensidade
        return self._accao