#encoding: utf-8
class Sistema3x3(object):
	def calcular(self,m):
		#inicializacion de variables
		self.matriz3=[]
		self.fila3=[]
		self.matriz=m

		#pasar a una matriz 3x3
		for x in xrange(0,3):
			self.fila3=[]
			for y in xrange(0,3):
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
			#determinante en z
			self.pasarColumna4(2)
			self.detz=self.calcularDeterminante()
			#hallar y
			self.z=self.detz/self.detp
			print"la respuesta es:"
			print "x="+str(self.x)+"\ny="+str(self.y)+"\nz="+str(self.z)
			a=[]
			a.append(self.x)
			a.append(self.y)
			a.append(self.z)
			return a
	def pasarafila2(self):
		self.matriz2=[]
		for x in xrange(0,3):
			self.fila2=[]
			for y in xrange(0,3):
				self.fila2.append(self.matriz[x][y])
			self.matriz2.append(self.fila2)

	def pasarColumna4(self,n):
		self.matriz2=[]
		for x in xrange(0,3):
			self.fila2=[]
			for y in xrange(0,3):
				if y==n:
					self.fila2.append(self.matriz[x][3])
				else:
					self.fila2.append(self.matriz[x][y])
			self.matriz2.append(self.fila2)

	def calcularDeterminante(self):
		c=1
		a=1
		b=1
		for y in xrange(0,3):
			a=self.matriz2[y][y]*a
		for x in xrange(0,3):
			if x==2:
				b=float(self.matriz2[x][0]*b)
			else:
				b=float(self.matriz2[x][x+1]*b)
		for x in xrange(0,3):
			if x==0:
				c=float(c*self.matriz2[x][x+2])
			else:
				c=float(c*self.matriz2[x][x-1])
		r1=a+b+c
		a=1
		b=1
		c=1
		d=2
		for x in xrange(0,3):
			a=float(self.matriz2[x][d]*a)
			d=d-1
		for x in xrange(0,3):
			if x==0:
				b=float(self.matriz2[x][x+1] *b)
			if x==1:
				b=float(self.matriz2[x][x-1]*b)
			if x==2:
				b=float(self.matriz2[x][x]*b)
		
		for x in xrange(0,3):
			if x==0:
				c=float(self.matriz2[x][x]*c)
			if x==1:
				c=float(self.matriz2[x][x+1]*c)
			if x==2:
				c=float(self.matriz2[x][x-1]*c)
		r2=a+b+c
		return r1-r2