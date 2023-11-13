"""
Classe MecUtil:
    classe que, juntamente com a classe pdm.py, implementam as funcoes necessárias para realizar o processo de decisão de markov.

"""

class MecUtil():

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama #double
        self.__delta_max = delta_max #int

    def utilidade(self):
        #estados do modelo, accoes possiveis a certo estado
        S, A = self.__modelo.S, self.__modelo.A #utilizar referência
        #gerador que inicializa um dicionario com o numero de estado no modelo, 
        #todos a zero
        U = {s:0.0 for s in S()} #invocar funcao

        while True:
            #copia da estrutura (primeiro nível)
            Uant = U.copy()
            #diferenca 
            delta = 0
            #para cada estado é atualizada a utilidade 
            for s in S():
                #maior valor de utilidade presente na lista de accoes 
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0) #valor de omissao a 0 caso nao haja nenhuma accao
                delta = max(delta, abs(U[s] - Uant[s])) #maior valor entre delta e diferenca em absoluto da diferença da utilidade anterior com a atual
            
            #se novo delta for menor que o delta max anterior sai do loop e retorna a utilidade
            if delta <= self.__delta_max:
                break

        return U
    
    #utilidade de um estado fazer uma accao
    #vai ser escolhida a accao que tem a maior utilidade
    """
    def util_accao(self, s, a, U):
        
        T, R, sn = self.__modelo.T, self.__modelo.R, a.aplicar(s)
        #alterar
        utilidade = 0
        if sn:
            utilidade += (T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]))
        return utilidade
    """

    def util_accao(self, s, a, U):
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        return sum( T(s,a,sn) * ( R(s,a,sn) ) + self.__gama * U[sn] for sn in suc(s, a))
