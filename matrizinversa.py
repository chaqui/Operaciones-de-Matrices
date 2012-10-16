from Operaciones import Operacion

class MatrizInversa(Operacion):
	def function():
		pass
	def matrizinversa(self):
		self.PedirMatriz()
		self.matriz2=[]
		self.filas2=[]
		for x in xrange(0,self.columna):
			for y in range(0,self.fila):
				a=self.matriz[y][x]
				self.filas2.append(a)
			self.matriz2.append(self.filas2)
			self.filas2=[]
		print "el resultado es el siguiente:"
		for x in self.matriz2:
			print x
matriz=MatrizInversa()
matriz.matrizinversa()