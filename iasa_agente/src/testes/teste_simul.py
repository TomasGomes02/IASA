from sae import Controlo
from sae import Simulador

"""

"""

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("Processar")

"""

"""

controlo = ControloTeste()

Simulador(1, controlo).executar()

#set PYTHONPATH=src;src\lib

#python src\testes\teste_simul.py