class No():

    def __init__(self, estado, operador=None, antecessor=None):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor

        #se existir antecessor, profundidade++ e custo = ao custo do antecessor + o atual
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
            self.__custo = antecessor.custo + operador.custo(antecessor.estado, estado)
        #se nao existir antecessor sabemos que o nó e o raiz e portanto nao tem profundidade nem custo
        else:
            self.__profundidade = 0
            self.__custo = 0

        

    #Getters dos atributos privados
    @property
    def profundidade(self):
        return self.__profundidade
        
    @property
    def custo(self):
        return self.__custo
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor
    #utilizacao do operador less than (<)
    def __lt__(self, no):
        return self.custo < no.custo
    
