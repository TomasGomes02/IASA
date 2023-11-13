from sae.simulador import Simulador

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.comport_comp import ComportamentoComp
from ecr.hierarquia import Hierarquia
from controlo_react.reaccoes.recolher import Recolher

"""


"""

teste = [Recolher()]


controlo = ControloReact(Hierarquia(teste))

Simulador(1, controlo).executar()

#set PYTHONPATH=src;src\lib

#python src\testes\teste_react.py
