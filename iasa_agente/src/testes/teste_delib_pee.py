from sae.simulador import Simulador
from plan.plan_pee.planeador_pee import PlaneadorPee
from controlo_delib.controlo_delib import ControloDelib
"""

"""

planeador = PlaneadorPee()
planeador.set_heuristica("Distancia")
#planeador.set_heuristica("Manhatam")
controlo = ControloDelib(planeador)

Simulador(4, controlo).executar()

#set PYTHONPATH=src;src\lib

#python src\testes\teste_delib_pee.py