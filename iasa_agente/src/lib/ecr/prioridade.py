from ecr.comport_comp import ComportamentoComp

"""
Classe Prioridade: 
    As respostas são seleccionadas
    de acordo com uma prioridade 
    associada que varia ao longo da 
    execução


"""

class Prioridade(ComportamentoComp):

    """
    Comportamentos escolhidos de acordo com a sua prioridade, que neste caso é um atributo de accoes,
    utilizando-se assim a expressao accao.prioridade a obtermos.     
    Recorre-se a uma função lambda, uma funcao transformativa, para avaliar a accao com a maior prioridade.
    
    """

    def selecionar_accao(self, accoes):

        if accoes is not None :

            return max(accoes, key=lambda accao: accao.prioridade)
            
        