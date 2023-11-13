from lib.pee.mec_proc.solucao import Solucao
from lib.pee.melhor_prim.procura_custo_uniforme import ProcuraCustoUnif
from lib.pee.prof.procura_profundidade_iter import ProcuraProfundidadeIter
from lib.pee.prof.procura_profundidade_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj

class PlaneadorTrajeto():
    
    def planear(ligacoes, loc_inicial, loc_final):

        #instancia de problema com as caracteristicas recebidas nos parametros de entrada
        prob = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final) 

        #mecanismo de procura utilizado é procura custo uniforme
        #mec_proc = ProcuraCustoUnif() # - FUNCIONA
        #mec_proc = ProcuraProfLim() # - FUNCIONA
        #mec_proc = ProcuraProfundidadeIter() # - FUNCIONA
        mec_proc = ProcuraProfundidade() # - FUNCIONA
        #mec_proc = ProcuraLargura() #- FUNCIONA

        #gerar uma solucao utilizando o método procura do mecanismo de procura que recebe um problema
        #e retorna uma solucao
        solucao = mec_proc.procurar(prob)
        print('Complexidade Temporal: ' + str(mec_proc.complexidade_temporal))
        print('Complexidade Espacial: ' + str(mec_proc.complexidade_espacial))
        return solucao
    

   