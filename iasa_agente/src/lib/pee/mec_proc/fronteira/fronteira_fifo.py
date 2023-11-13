from .fronteira import Fronteira

class FronteiraFIFO(Fronteira):

    def inserir(self, no):
        self._nos.append(no)
