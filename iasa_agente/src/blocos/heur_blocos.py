from lib.pee.melhor_prim.aval.heuristica import Heuristica

class HeurBlocos(Heuristica):
    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        #contador que é incrementado sempre que haja elementos diferentes nas pilhas
        #no contexto do problema representa 
        dif = sum((x != y) for x, y in zip(estado.pilhas[0], self.__estado_final[0]))
        return dif