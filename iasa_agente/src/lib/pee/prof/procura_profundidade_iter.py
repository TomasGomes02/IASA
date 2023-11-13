from pee.prof.procura_profundidade_lim import ProcuraProfLim

class ProcuraProfundidadeIter(ProcuraProfLim):

    def procurar(self, problema, inc_prof=1, limit_prof=100):
        
        #profundidade inicial
        prof = 0
        
        #enquanto o limite da profundidade nao for excedido
        while prof <= limit_prof:
            
            #setter da nova profundidade (1, 2, 3, ..., n)
            self.prof_max = prof

            #a cada iteracao verifica se há solucao
            solucao = super().procurar(problema)

            #incrementa o limite de profundidade
            prof+=inc_prof

            #se existir solucao retorna-a
            if solucao:
                return solucao
        
        #se nao existir solucao retorna None
        return None
    
    """ Resolucao professor 

    def procurar(self, problema, inc_prof=1, limit_prof=100):     
        for profundidade in range(0, limit_prof-1):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao
    """
