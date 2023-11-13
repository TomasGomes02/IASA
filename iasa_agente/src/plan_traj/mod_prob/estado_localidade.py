from lib.mod.estado import Estado
"""

    Classe que atribui uma localidade a um estado
    Converte os conceitos do dominio do problema para conceitos do dominio mecanismo, adaptando os conceitos
    "Transforma" nomes de localidades para estados"""

class EstadoLocalidade(Estado):

    #É inicializada a localidade como atributo privado
    def __init__(self, localidade):
        self.__localidade = localidade

    #A localidade é identificada a partir deste id_valor que retorna o ultimo
    #valor de uma string de caracteres que neste caso será convertida para int() pois
    #as localidades seguem a sintaxe => Loc-0, Loc-1, Loc-2, etc
    def id_valor(self):
        return int(self.localidade[-1])

    @property
    def localidade(self):
        return self.__localidade


#id valor retorna numero inteiro correspondente ao numero da localidade
#ex --> localidade 0 retorna 0 etc