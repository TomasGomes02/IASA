from lib.pee.mec_proc.solucao import Solucao
from lib.pee.melhor_prim.procura_custo_uniforme import ProcuraCustoUnif
from lib.pee.prof.procura_profundidade_iter import ProcuraProfundidadeIter
from lib.pee.prof.procura_profundidade_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.larg.procura_largura import ProcuraLargura

from mod_prob.problema_deposito import ProblemaDeposito

class PlaneadorEncher():
    
    
    def planear(self, ligacoes, valor_inicial, valor_final):

        solucoes = []
        compx = []

        mecanismos_procura = [
                        ProcuraCustoUnif(),
                        ProcuraProfLim(),
                        ProcuraProfundidadeIter(),
                        #ProcuraProfundidade(),
                        ProcuraLargura()
                        ]

        #instancia de problema com as caracteristicas recebidas nos parametros de entrada
        prob = ProblemaDeposito(ligacoes, valor_inicial, valor_final) 

        for mecs in mecanismos_procura:
            mec_proc = mecs 

            #gerar uma solucao utilizando o método procura do mecanismo de procura que recebe um problema
            #e retorna uma solucao
            solucao = mec_proc.procurar(prob)

            compx.append((str(mec_proc.complexidade_espacial), str(mec_proc.complexidade_temporal)))
            
            solucoes.append(solucao)

        return solucoes, compx
    