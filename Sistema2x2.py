#encoding: utf-8
class Sistema2x2(object):
	def calcular(self,m):
		#inicializacion de variables
		self.matriz3=[]
		self.fila3=[]
		self.matriz=m

		#pasar a una matriz 3x3
		for x in xrange(0,2):
			self.fila3=[]
			for y in xrange(0,2):
				self.fila3.append(self.matriz[x][y])
			self.matriz3.append(self.fila3)
		#calcular determinante
		self.pasarafila2()
		self.detp=self.calcularDeterminante()
		if self.detp==0:
			return 0
		else:
			#determinante en x
			self.pasarColumna4(0)
			self.detx=self.calcularDeterminante()
			#hallar x
			self.x=self.detx/self.detp
			#determinante en y
			self.pasarColumna4(1)
			self.dety=self.calcularDeterminante()
			#hallar y
			self.y=self.dety/self.detp
			print"la respuesta es:"
			print "x="+str(self.x)+"\ny="+str(self.y)
			a=[]
			a.append(self.x)
			a.append(self.y)
			return a
	def pasarafila2(self):
		self.matriz2=[]
		for x in xrange(0,2):
			self.fila2=[]
			for y in xrange(0,2):
				self.fila2.append(self.matriz[x][y])
			self.matriz2.append(self.fila2)

	def pasarColumna4(self,n):
		self.matriz2=[]
		for x in xrange(0,2):
			self.fila2=[]
			for y in xrange(0,2):
				if y==n:
					print str(n)+"y: "+str(y)
					self.fila2.append(self.matriz[x][2])
				else:
					self.fila2.append(self.matriz[x][y])
			self.matriz2.append(self.fila2)
			print self.matriz2
	def calcularDeterminante(self):
		a=1
		b=1
		for y in xrange(0,2):
			a=float(self.matriz2[y][y]*a)
		for x in xrange(0,2):
			if x==0:
				b=float(self.matriz2[x][1]*b)
			else:
				b=float(self.matriz2[x][0]*b)
		r1=a-b
		print r1
		return r1