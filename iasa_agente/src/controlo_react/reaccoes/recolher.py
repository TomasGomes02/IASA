from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar

from ecr.hierarquia import Hierarquia

class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([AproximarAlvo(), EvitarObst(), Explorar()])