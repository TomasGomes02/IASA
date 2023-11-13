from mod.estado import Estado

class EstadoAgente(Estado):

    #posicao é um tuplo (x,y)
    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao)

    #read-only
    @property
    def posicao(self):
        return self.__posicao

    #identificador unico inteiro
    def id_valor(self):
        return self.__id_valor
