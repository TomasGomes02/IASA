
from lib.pee.mec_proc.no import No
from pee.mec_proc.mecanismo_procura import MecanismoProcura
class ProcuraGrafo(MecanismoProcura):
    
    @property
    def complexidade_espacial(self):
        return len(self._explorados)


    #iniciar memoria do mecanismo procura + criar um dicionario de explorados, vazio
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}

    #guardar no no dicionario "explorados" e na fronteira
    def _memorizar(self, no):
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)
            
            #complexidade espacial - máximo de nós mantidos em memória
            #verifica se a nova complexidade é maior que a antiga e caso seja, substitui-a
            #self.complexidade_espacial = max(len(self._explorados), self.complexidade_espacial)

    def _manter(self, no):
        #um nó cujo estado ja exista nao é para manter
        return no.estado not in self._explorados
    
    
    
    
