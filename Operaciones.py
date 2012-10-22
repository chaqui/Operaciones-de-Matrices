#encoding: utf-8
class Operacion:
	"""docstring for ClassName"""
	def __init__(self):
		pass
	def pedirDimensiones(self):
		Dimensiones=raw_input("Pofavor ingrese las dimensiones de la  matriz \n")
		self.fila=""
		self.columna=""
		self.bandera = True
		for letra in Dimensiones:
			if letra=="x":
				self.bandera=False
			if self.bandera==True :
				self.fila=self.fila+letra
			if self.bandera==False:
				if letra!="x":	
					self.columna=self.columna+letra
		self.fila=int(self.fila)
		self.columna= int(self.columna)
	def PedirMatriz(self):
		r=1
		while(r==1) :
			self.filas=[]
			self.matriz=[]
			self.pedirDimensiones()
			for x in xrange(0,self.fila):
				print("Porfavor ingrese la fila "+str(x+1)+": ")
				for y in xrange(0,self.columna):
					y=int(raw_input("porfavor ingrese la columna "+str(y+1)+": "))
					self.filas.append(y)
				self.matriz.append(self.filas)	
				self.filas=[]
			print "su matriz queda de la siguiente forma:"
			for x in self.matriz:
				print x
			r=raw_input("esta bien su matriz o desea repetir 1=si / 0= no ")

