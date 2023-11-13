

from planeador.ligacao import Ligacao
from planeador.planeador_trajeto import PlaneadorTrajeto
from planeador.trajeto import Trajeto

LOC_INICIAL = "loc0"
LOC_FINAL = "loc4"

#implementar heuristica para heuristica

LIGACOES = [
            Ligacao('loc0', 'loc1', 5),
            Ligacao('loc0', 'loc2', 25),
            Ligacao('loc-1', 'loc-3', 12),
            Ligacao('loc-1', 'loc-6', 5),
            Ligacao('loc-2', 'loc-4', 30),
            Ligacao('loc-3', 'loc-2', 10),
            Ligacao('loc-3', 'loc-5', 5),
            Ligacao('loc-4', 'loc-3', 2),
            Ligacao('loc-5', 'loc-6', 8),
            Ligacao('loc-5', 'loc-4', 10),
            Ligacao('loc-6', 'loc-3', 15),
                                            ]

def teste_plan_traj():    

    planeador = PlaneadorTrajeto

    solucao = planeador.planear(LIGACOES, LOC_INICIAL, LOC_FINAL)
    
    if solucao:
        Trajeto(solucao).mostrar()

teste_plan_traj()


#set PYTHONPATH=src;src\lib

#python src\plan_traj\teste_plan_traj.py
