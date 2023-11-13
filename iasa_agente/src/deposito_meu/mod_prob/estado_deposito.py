from lib.mod.estado import Estado
"""

"""

class EstadoDeposito(Estado):

    def __init__(self, deposito):
        self.__deposito = deposito


    def id_valor(self):
        return self.__deposito

    @property
    def valor(self):
        return self.__deposito
