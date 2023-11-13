from controlo_react.reaccoes.evitar.estimulo.estimulo_obst import EstimuloObst

from ecr.reaccao import Reaccao

class EvitarDir(Reaccao):

    def __init__(self, direccao, resposta):
        
        super().__init__(EstimuloObst(direccao), resposta)