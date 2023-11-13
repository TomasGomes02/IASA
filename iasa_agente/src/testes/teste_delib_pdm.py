from controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Simulador

controlo = ControloDelib(PlaneadorPDM(0.60))
Simulador(4, controlo).executar()

#set PYTHONPATH=src;src\lib

#python src\testes\teste_delib_pdm.py