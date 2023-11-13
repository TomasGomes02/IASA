from pee.prof.procura_profundidade import ProcuraProfundidade

"""

"""

class ProcuraProfLim(ProcuraProfundidade):

	def __init__(self, prof_max=100):
		super().__init__()
		self.__prof_max = prof_max 

	#getter do atributo prof_max
	@property 
	def prof_max(self):
		return self.__prof_max

	#setter do atributo prof_max
	@prof_max.setter
	def prof_max(self, prof_max):
		self.__prof_max = prof_max	
    
	#Expande o nó se a sua profundidade for inferior à profundidade máxima da procura
	def _expandir(self, problema, no):
		if no.profundidade < self.prof_max:
			yield from super()._expandir(problema, no)

	"""
	Verifica se nó corresponde a um ciclo no ramo 
	respectivo, para evitar a expansão de nós referentes a 
	estados já explorados (não evita ciclos em relação a 
	outros ramos)

	"""

	"""
	def _ciclo(self, no):

		#Enquanto existir antecessor
		while no.antecessor!=None:

			#se o estado do no antecesssor for o mesmo do estado do no atual significa que ja foi explorado
			if no.antecessor.estado == no.estado:
				return True
			
			#atualiza o no antecessor para o atual
			no = no.antecessor
			
		#se nao, é porque nao foi explorado
		return False
	"""


	def __estados_antecessores(self, no):

		antecessor = no.antecessor

		while antecessor:

			yield antecessor.estado
			antecessor = antecessor.antecessor


	def _ciclo(self, no):

		return no.estado in self.__estados_antecessores(no)

	
    #Memoriza nó se nao corresponder a um ciclo
	def _memorizar(self, no):
		if self._ciclo(no) == False:
		    super()._memorizar(no)

	
