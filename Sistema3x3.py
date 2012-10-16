class Sistema3x3(object):

	def pedirMatriz(self):
		self.filas=[]
		self.matriz=[]
		self.res=0
		while(self.res==0) :
			for x in xrange(0,3):
				self.filas=[]
				for y in xrange(0,4):
					if y==0:
						p="x"
					if y==1:
						p="y"
					if y==2:
						p="z"
					if y==3:
						self.columna=int(raw_input("Porfavor ingrese la variable entera :"))
					else:
						self.columna=int(raw_input("Porfavor ingrese "+p+str(x+1)+" :"))
					self.filas.append(self.columna)
				self.matriz.append(self.filas)
			for x in self.matriz:
				print x
			self.res=int(raw_input("esta bien la matriz si=1 / no=0"))
			if self.res==0:
				print"vuelva a entrar los datos"

	def calcular(self):
		#inicializacion de variables
		self.matriz3=[]
		self.fila3=[]
		self.pedirMatriz()

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
			print"la ecuacion tiene infinitas respuestas"
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
			print "x="+str(self.x)+"\ny="+str(self.y)+"\nz="+str(self.z)
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
				b=self.matriz2[x][0]*b
			else:
				b=self.matriz2[x][x+1]*b
		for x in xrange(0,3):
			if x==0:
				c=c*self.matriz2[x][x+2]
			else:
				c=c*self.matriz2[x][x-1]
		r1=a+b+c
		a=1
		b=1
		c=1
		d=2
		for x in xrange(0,3):
			a=self.matriz2[x][d]*a
			d=d-1
		for x in xrange(0,3):
			if x==0:
				b=self.matriz2[x][x+1]*b
			if x==1:
				b=self.matriz2[x][x-1]*b
			if x==2:
				b=self.matriz2[x][x]*b
		
		for x in xrange(0,3):
			if x==0:
				c=self.matriz2[x][x]*c
			if x==1:
				c=self.matriz2[x][x+1]*c
			if x==2:
				c=self.matriz2[x][x-1]*c
		r2=a+b+c
		return r1-r2
sistema = Sistema3x3()
sistema.calcular()