from deposito.problema_deposito import ProblemaDeposito
from deposito_meu.encher import Deposito
from lib.pee.melhor_prim.procura_custo_uniforme import ProcuraCustoUnif
from lib.pee.prof.procura_profundidade_iter import ProcuraProfundidadeIter
from lib.pee.prof.procura_profundidade_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.larg.procura_largura import ProcuraLargura


VOLUME_INICIAL = 0
VOLUME_FINAL = 9

#instanciar o problema que recebe o volume inicial e o final do deposito
problema = ProblemaDeposito(VOLUME_INICIAL, VOLUME_FINAL)

#instanciar o mecanismo de procura a utilizar
mec_proc = ProcuraProfLim()

solucao = mec_proc.procurar(problema)

if solucao:
	Deposito(solucao).mostrar()

#set PYTHONPATH=src;src\lib
#python src\deposito\teste_deposito.py

#lim
#larg
#custo
#iter