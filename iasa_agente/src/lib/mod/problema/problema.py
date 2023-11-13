from abc import ABC, abstractmethod


#Problema:
    #É constituido por um estado inicial, em que se inicia o problema,
    #vários operadores que vão sendo iterados até ao objetivo e a função de teste do objetivo.



class Problema(ABC):

    
    #operadores = lista de operadores

    def __init__(self, estado_inicial, operadores):
        
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @property
    def estado_inicial(self):
        return self.__estado_inicial

    @property
    def operadores(self):
        return self.__operadores

    @abstractmethod
    def objetivo(self, estado):
        raise NotImplementedError


