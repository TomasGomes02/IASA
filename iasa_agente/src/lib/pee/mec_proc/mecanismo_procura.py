from abc import ABC, abstractmethod, abstractproperty
from mod.estado import Estado

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
Um mecanismo de procura, permite a solução de um problema, neste caso, 
    utilizando fronteiras de exploração para memorizar os nós explorados.
"""


class MecanismoProcura(ABC):
    
    """
    A nossa estrutura de dados é formada por 3 principais "objetos":

    A raiz, o nó inicial que nao tem nem operador nem atecessor, ou seja, o primeiro.

    Nós interiores, que possuem nós sucessores a estes.
    
    Folhas, nós na "ponta" da arvore de procura, ou seja, nós que não têm sucessores.

    Cada elemento Nó contém a informação relativa ao estado,
        ao operador que gerou o estado em que o nó se encontra, 
        o antecessor, o nó anterior na árvore de procura, 
        a profundidade do nó, relativo à árvore de procura e,
        o custo do percurso correspondente ao nó.

    Properties de complexidade tempora e espacial
    """
    
    @property
    #Número de Nós processados
    def complexidade_temporal(self):
        return self.__complexidade_temporal
        
    
    @abstractproperty
    #Máximo de nós mantidos em memória
    def complexidade_espacial(self):
        return self.__complexidade_espacial
    
    """
    @complexidade_espacial.setter
    def complexidade_espacial(self, value):
        self.__complexidade_espacial = value
    """
    @complexidade_temporal.setter
    def complexidade_temporal(self, value):
        self.complexidade_temporal = value
    
    def __init__(self, fronteira):
        self._fronteira = fronteira
        #self.__complexidade_espacial = 0
        self.__complexidade_temporal = 0
    
    #2 tipos de memoria:
     #   - fronteira
      #  - explorados
    
    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    
    @abstractmethod
    def _memorizar(self, no):
        """"""
    
    def procurar(self, problema):

        #inicia a memoria
        self._iniciar_memoria()
        #inserir um nó inicial com o estado do problema e memoriza-se esse nó
        no = No(problema.estado_inicial)
        self._fronteira.inserir(no)
        #self._memorizar(no)
        #ciclo de enquanto a fronteira nao estiver vazia
        while not(self._fronteira.vazia == True):
            #incrementar complexidade temporal a cada ciclo de exploraçao
            
            
            #retirar primeiro no da fronteira
            no = self._fronteira.remover()
            #verificamos se é objetivo
    
            if problema.objetivo(no.estado):
            #se for, retornamos a solucao
                return Solucao(no)
            
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)
            
            self.__complexidade_temporal = self.__complexidade_temporal + 1
            
            


    
    def _expandir(self, problema, no):
        
        #por cada operador no problema
        for operador in problema.operadores:
            #aplicar operador ao estado do no, obtendo um estado sucessor
            estado_sucessor = operador.aplicar(no.estado) 
            #se existir estado sucessor, libertamos o no
            if estado_sucessor:
                #yield liberta o valor em cada iteracao
                yield No(estado_sucessor, operador, no)


