from plan_traj.mod_prob.estado_localidade import EstadoLocalidade
from plan_traj.mod_prob.operador_ligacao import OperadorLigacao
from lib.mod.problema.problema import Problema

class ProblemaPlanTraj(Problema):

    def __init__(self, ligacoes, loc_inicial, loc_final):

        super().__init__(EstadoLocalidade(loc_inicial), [OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo) for ligacao in ligacoes])
                
        self.__estado_final = EstadoLocalidade(loc_final)

    #Retorna false caso o estado nao seja o objetivo e retorna true caso seja
    def objetivo(self, estado):

        return estado == self.__estado_final
    