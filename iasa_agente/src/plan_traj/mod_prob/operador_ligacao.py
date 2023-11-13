
from lib.mod.operador import Operador
from plan_traj.mod_prob.estado_localidade import EstadoLocalidade

"""
    Classe Operador Ligacao
    Converte os conceitos do dominio do problema para conceitos do dominio mecanismo, adaptando os conceitos
    "Transforma" ligacoes entre localidades em operacoes 
    
    """


class OperadorLigacao(Operador):


    def __init__(self, origem, destino, custo):
        self.__estado_origem = EstadoLocalidade(origem)
        self.__estado_destino = EstadoLocalidade(destino)
        
        self.__custo = custo
    """
    
    Onde está codificada a transformaçao que o operador representa
    """
    
    def aplicar(self, estado):
        if estado == self.__estado_origem:
            return self.__estado_destino

    """
    Retornar o custo do operador, nao sao utilizados os parametros
    estado e estado_suc mas estao presentes para respeitar o contrato com a classe Operador"""
    
    def custo(self, estado, estado_suc):
        return self.__custo