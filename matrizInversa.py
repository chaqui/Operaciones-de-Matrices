#encoding: utf-8
from Sistema3x3 import Sistema3x3
class MatrizInversa(Sistema3x3):
	def calcularM(self,m):
		self.filar=[]
		self.matr=[]
		print "Inversa de matriz 3x3"
		self.matriz=m
		self.pasarafila2()
		self.detp=self.calcularDeterminante()
		if self.detp==0:
			print "no tiene inversa"
			return []
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
			print self.matr
			return self.matr
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