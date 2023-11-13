from .comportamento import Comportamento

"""
Classe Reaccao
    Esta classe associa estímulo a resposta

"""

class Reaccao(Comportamento):

    """
    Construtor da classe Reaccao
        Recebe um estímulo e uma resposta.
        É utilizado "__" de maneira a declarar o atributo privado, de modo a diminuir a sua visibilidade.

    """

    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    """
    Método activar():
        Recebe como argumento uma percepcao, retornando uma 
        acção, consoante a condicao definida.
        Começase por guardar a intensidade na sua respetiva variável,
        e, caso esta seja maior que 0, será retornada a resposta gerada.

    """
    
    def activar(self, percepcao):

        intensidade = self.__estimulo.detectar(percepcao)

        if intensidade > 0:
            return self.__resposta.activar(percepcao, intensidade)