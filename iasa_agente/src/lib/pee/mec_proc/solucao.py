
class Solucao():

    @property
    def dimensao(self):
        return len(self.__percurso)

    @property
    def percurso(self):
        return self.__percurso

    def __init__(self, no_final):
        #iniciar percurso
        self.__percurso = []
        no = no_final
        #enquanto existirem nós
        while no:
            #inserir no percurso e defini-lo como antecessor, no inicio
            self.__percurso.insert(0, no)
            no = no.antecessor
        
    
    def remover(self):
        #se existir percurso
        if self.__percurso:
            #remover primeiro do percurso
            return self.__percurso.pop(0)
    
    #iterador do percurso
    def __iter__(self):
        return iter(self.__percurso)
    
    #retorna o no do percurso no indice recebido
    def __getitem__(self, index):
        return self.__percurso[index]
     
