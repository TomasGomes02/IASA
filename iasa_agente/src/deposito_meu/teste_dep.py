
from ligacao_dep import Recipiente
from encher import Deposito
from planeador_encher import PlaneadorEncher

VOL_INICIAL = 0
VOL_FINAL = 9

#implementar heuristica para heuristica

LIGACOES = [

            Recipiente(2, 4),
            Recipiente(3, 9),
                                    ]

indixes = [               "ProcuraCustoUnif", 
                          "ProcuraProfLim", #NAO FUNCIONA BEM
                          "ProcuraProfundidadeIter",
                          #"ProcuraProfundidade",
                          "ProcuraLargura"]


def teste_encher():    


    planeador = PlaneadorEncher()
    print(" Volume inicial : ", VOL_INICIAL, '\n', 
          "Volume Final: ", VOL_FINAL)
    
        
    solucoes, compx = planeador.planear(LIGACOES, VOL_INICIAL, VOL_FINAL)
    for i in range(len(solucoes)):
        if solucoes[i]:
            print(indixes[i])

            Deposito(solucoes[i]).mostrar()

            print("Complexidade Espacial ", compx[i][0])
            print("Complexidade Temporal ", compx[i][1])
            print("\n")


teste_encher()


#set PYTHONPATH=src;src\lib

#python src\deposito\teste_dep.py