from lib.pee.mec_proc.solucao import Solucao
class Trajeto():
    #lista de nomes e localidades
    def __init__(self, solucao):
        self.__localidades = [no.estado.localidade for no in solucao]
        #self.__localidades = []
        #for no in solucao:
        #   self.__localidades.append(no)

        self.__custo = solucao.percurso[-1].custo
        self.__dimensao = solucao.dimensao

    #Solucao: [...]
    #Dimensao: 10
    #Custo: 50
    def mostrar(self):
        print("Solucao : " , self.__localidades, "\n",  "Dimensao: ", self.__dimensao, "\n", "Custo: ", self.__custo)
