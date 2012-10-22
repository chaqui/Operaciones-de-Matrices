#encoding: utf-8
from Sistema3x3 import Sistema3x3
class MatrizInversa(Sistema3x3):

	def pedirMatriz(self):
		self.filas=[]
		self.matriz=[]
		self.res=0
		while(self.res==0) :
			for x in xrange(0,3):
				self.filas=[]
				for y in xrange(0,3):
					self.columna=int(raw_input("Porfavor ingrese "+str(x+1)+" "+str(y+1)+" :"))
					self.filas.append(self.columna)
				self.matriz.append(self.filas)
			for x in self.matriz:
				print x
			self.res=int(raw_input("esta bien la matriz si=1 / no=0"))
			if self.res==0:
				print"vuelva a entrar los datos"
	def calcularM(self):
		self.filar=[]
		self.matr=[]
		print "Inversa de matriz 3x3"
		self.pedirMatriz()
		self.pasarafila2()
		self.detp=self.calcularDeterminante()
		if self.detp==0:
			print "no tiene inversa"
		else:
			print self.detp
			for x in xrange(0,3):
				self.filar=[]
				for y in xrange(0,3):
					if x==0 and y==1:
						a= self.calcularAdjunta(x,y)
						b= float(a*-1)
						self.adj =b/float(self.detp)
					elif x==1 and y==0:
						a= self.calcularAdjunta(x,y)
						b= float(a*-1)
						self.adj =b/float(self.detp)
					elif x==1 and y==2:
						a= self.calcularAdjunta(x,y)
						b= float(a*-1)
						self.adj =b/float(self.detp)
					elif x==2 and y==1:
						a= self.calcularAdjunta(x,y)
						b= float(a*-1)
						self.adj =b/float(self.detp)
					else:
						b= float(self.calcularAdjunta(x,y))
						self.adj =b/self.detp
					self.filar.append(self.adj)
				self.matr.append(self.filar)
			print "el resultado es:"
			for x in self.matr:
				print x
	def calcularAdjunta(self,a,b):
		matriza=[]
		filaa=[]
		for x in xrange(0,3):
			filaa=[]
			if x!=a:
				for y in xrange(0,3):
					if y!= b:
						filaa.append(self.matriz2[x][y])
				matriza.append(filaa)
		return self.Adjunta(matriza)
	def Adjunta(self,matriz):
		a=matriz[0][0]*matriz[1][1]
		b=matriz[1][0]*matriz[0][1]
		return a-b