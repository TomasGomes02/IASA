from blocos.planeador_blocos import PlaneadorBlocos
from blocos.mostrar_blocos import MostrarBlocos
from blocos.problema_blocos import ProblemaBlocos

inicial = [[2,3,1], [], []]
final = [[1,2,3], [], []] 

#gera problema


#instancia um objeto planeador
planeador = PlaneadorBlocos()

#planeador gera solucao para o problema
solucao = planeador.planear(inicial, final)
if solucao:
    MostrarBlocos(solucao).mostrar()

#set PYTHONPATH=src;src\lib

#python src\blocos\teste_blocos.py