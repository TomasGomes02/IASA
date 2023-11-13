from sae import Elemento

class MecDelib():

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    #gerar os objetivos do agente
    def deliberar(self):
        #criar lista de objetivos em que cada elemento da lista é uma instancia de estado caso seja um alvo
        objectivos = [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        
        if objectivos:

            #retorna uma lista de objetivos ordenados pela distancia ao agente
            objectivos.sort(key=self.__modelo_mundo.distancia)

            return objectivos