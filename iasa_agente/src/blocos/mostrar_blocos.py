class MostrarBlocos():

    def __init__(self, solucao):
        self.__operadores = [no.operador for no in solucao][1:]
        self.__custo = solucao[-1].custo

    def mostrar(self):
        print("Solução: " + str(self.__operadores))
        print("Dimensão: " + str(len(self.__operadores)))
        print("Custo: " + str(self.__custo))
