from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao

import random

"""
Classe RespostaEvitar

"""
""""""
class RespostaEvitar(RespostaMover):

    def __init__(self, dir_inicial = Direccao.ESTE):
        super().__init__(dir_inicial)
        self.__direccoes = list(Direccao)


    def activar(self, percepcao, intensidade):

        """ 
        Vai se alterando o contacto com o obstaculo até não haver e só depois de não haver contacto,
        mudamos a direcao.
        """
        contacto_obst = percepcao.contacto_obst(self._accao.direccao) 
        if contacto_obst: #existe contacto com o obstaculo
            contacto_obst = not self.__alterar_direccao(percepcao) #mudar de direcao
                
        if not contacto_obst: #nao existe contacto com o obstaculo
            return super().activar(percepcao, intensidade) #mudar de direcao


    """
    Funcao privada ("__") que itera pela lista de direcoes e verifica se estao livres,
    com o auxilio da funcao contacto_obst que recebe a direccao a ser avaliada.
    
    """ 
    def __direccao_livre(self, percepcao):

        direccoes_livres = [dir for dir in self.__direccoes if not percepcao.contacto_obst(dir)]

        return random.choice(direccoes_livres)

    """
    Funcao privada ("__") que ativa/altera a direcao atual para a direcao livre, previamente escolhida
    
    """
    def __alterar_direccao(self, percepcao):

        #se retornar algum valor conta como True, se não, conta como False
        direccao_livre = self.__direccao_livre(percepcao)
        
        if(direccao_livre != None):
           
            self._accao.direccao = direccao_livre
            return self._accao.direccao

