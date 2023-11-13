#from lib.sae.

from .mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo

from sae import Controlo


class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__objectivos = None
        self.__modelo_mundo = ModeloMundo()
        self.__mecanismo_delib = MecDelib(self.__modelo_mundo)
        self.__planeador = planeador
        self.__plano = None
        
    def processar(self, percepcao):
        
        #atualiza o modelo do mundo com a percepcao que recebe ou se o plano nao existir/for uma lista vazia
        self.__assimilar(percepcao)
            
            #reconsidera
        if  self.__reconsiderar():
            #delibera de novo
            self.__deliberar()
            #faz um novo plano
            self.__planear()
            
        #debug
        self.__mostrar()

        #executa a acao
        accao = self.__executar()

        return accao

    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
    
    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__plano
    
    def __deliberar(self):
        self.__objectivos = self.__mecanismo_delib.deliberar()
    
    #gera um plano
    def __planear(self):
        #caso existam objetivos, é criado um plano a partir dos mesmos e do modelo do mundo
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        #caso nao existam, plano é definido a None como nao existindo
        else:
            self.__plano = None

    #retira accao a accao presente no plano resultante do planear
    def __executar(self):
        
        #caso exista plano
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            
            #retorna a accao associada ao operador
            return operador.accao
    
    #mostra o modelo do mundo e o plano
    def __mostrar(self):
        #super para ir buscar controlo do sae
        self.vista.limpar() #limpa a janela e so procede caso haja plano
        self.__modelo_mundo.mostrar(super().vista)
        if self.__plano:
            self.__plano.mostrar(super().vista)
        