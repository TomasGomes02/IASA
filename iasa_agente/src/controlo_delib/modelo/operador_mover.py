from lib.mod.operador import Operador
from mod.agente.estado_agente import EstadoAgente
from sae import Accao
import math


#No contexto do problema, este operador representa o movimento do agente no mundo
class OperadorMover(Operador):

    @property
    def ang(self):
        return self.__ang
    
    @property
    def accao(self):
        return self.__accao
    
    def __init__(self, modelo_mundo, direccao):
        self.__ang = direccao.value
        self.__accao = Accao(direccao)
        self.__modelo_mundo = modelo_mundo
        

    def aplicar(self, estado):
        
        #decomposicao do tuplo posicao 
        x, y = estado.posicao

        #calcular a variacao das coordenadas
        dx = round(self.accao.passo * math.cos(self.ang))
        dy = round(-1*self.accao.passo * math.sin(self.ang))

        #aplicar a variacao à posicao, resultando numa nova posicao
        nova_posicao = (x+dx, y+dy)

        #criacao de um novo estado do agente com a nova posicao anteriormente calculada
        novo_estado = EstadoAgente(nova_posicao)
        
        #se o estado for valido, ou seja, se estiver na lista de estados validos do objeto modelo_mundo
        #validar e retornar o novo estado
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado

    #distancia entre posicoes do estado e do estado sucessor mas com valor mínimo de 1
    def custo(self, estado, estado_succ):
        #print("ESTADO_SUC ", estado_succ)
        #print("ESTADO ", estado)
        
        distancia = math.dist(estado_succ.posicao, estado.posicao)
        #se distancia for menor que 1, retornar 1 que é o valor mínimo
        return max(distancia, 1)
        
    