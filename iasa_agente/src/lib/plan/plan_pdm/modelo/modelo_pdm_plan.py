from lib.pdm.modelo.modelo_pdm import ModeloPDM
from lib.plan.modelo.modelo_plano import ModeloPlano
"""
Classe ModeloPDMPlan:
    classe que, como o nome indica, modula o mundo de forma a ser possível chegar a uma solução, 
    utilizando o processo de Markov.
"""

class ModeloPDMPlan(ModeloPlano, ModeloPDM):
    
    def __init__(self, modelo_plan, objetivos, rmax=5000):
        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax
        self.__transicoes = {}
        
        for s in self.obter_estados():
            for a in self.obter_operadores():
                #Modelo determinista, só há uma transicao
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s, a)] = sn

    #métodos da interface ModeloPlano
    def obter_estado(self):
        return self.__modelo_plan.obter_estado() 
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
        
    #métodos da interface ModeloPDM
    def S(self):
        return self.obter_estados()
    
    def A(self, s):
        return self.obter_operadores()
    
    def T(self, s, a, sn):
        #retorna probabilidade 1 caso exista transicao visto que estamos a lidar com um modelo determinista
        #sn_trans = self.__transicoes.get((s, a))
        #return 1.0 if sn_trans == sn else 0.0
        return 1.0 if self.__transicoes.get((s, a)) == sn else 0.0

    
    def R(self, s, a, sn):
        
        r = -a.custo(s, sn)

        if sn in self.__objetivos:
            r += self.__rmax
            
        return r
    
    def suc(self, s, a):
        sn = self.__transicoes.get( (s, a) )
        return [sn] if sn else []