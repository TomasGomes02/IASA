from abc import ABC, abstractmethod

class Fronteira(ABC):

    @property
    def dim(self):
        return len(self._nos)

    @property
    def vazia(self):
        return len(self._nos) == 0

    #construtor chama metodo iniciar para nao ser redundante
    def __init__(self):
        self.iniciar()

    #inicia a lista de nós
    def iniciar(self):
        self._nos = []

    #insere na lista, metodo abstrato
    @abstractmethod
    def inserir(self, no):
        """"""

    #remove primeiro no da lista de nos
    def remover(self):
        return self._nos.pop(0)

    #retorna true se a lista estiver vazia
    
