
from controlo_delib.modelo.operador_mover import OperadorMover
from mod.agente.estado_agente import EstadoAgente
from sae import Direccao
import math

from plan.modelo.modelo_plano import ModeloPlano

class ModeloMundo(ModeloPlano):

    @property
    def alterado(self):
        return self.__alterado

    @property
    def elementos(self):
        return self.__elementos

    def __init__(self):
        self.__alterado = False
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]

    #getter do estado
    def obter_estado(self):
        return self.__estado
    
    #getter dos estados
    def obter_estados(self):
        return self.__estados
    
    #getter dos operadores
    def obter_operadores(self):
        return self.__operadores
    
    #getter do elemento pertencente ao dicionario de elementos 
    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao)
    
    #calcular distancia entre distancia atual e a distancia do estado recebido
    def distancia(self, estado):
        return round(math.dist(self.__estado.posicao, estado.posicao)) #pode estar errado
    
    #Caso haja mudanças no plano do mundo
    def actualizar(self, percepcao):
        
        self.__estado = EstadoAgente(percepcao.posicao)
        #se houver elementos novos vindos da percepcao
        if self.__elementos != percepcao.elementos:
            #atualizar elementos atuais com os vindos da percepcao
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes] #atualizar os estados validos para todas as posicoes validas da percepcao
            self.__alterado = True
        else:
            self.__alterado = False
        return 
    
    def mostrar(self, vista):
        
        #mostrar alvos e obstáculos
        vista.mostrar_alvos_obst(self.__elementos)
        #marcar a posicao dos mesmos
        vista.marcar_posicao(self.__estado.posicao)
        