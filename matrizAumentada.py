class MatrizAumentada(object):
	"""docstring for MatrizAumentada"""
	def procesar(self):
		x=0
		y=0
		z=0
		n=0
		nb=False
		ns=""
		self.fila=[]
		self.matriz=[]
		for i in xrange(0,3):
			x=0
			y=0
			z=0
			n=0
			ns=""
			nb=False
			self.fila=[]
			cad=str(self.pedirCadena(i))
			for letra in cad:
				if nb==False:
					if letra=="x":
						if ns=="+":
							x=x+1
						elif ns=="-":
							x=x-1
						elif ns=="":
							x=x+1
						else:
							x=x+float(ns)
						ns=""
					elif letra =="y":
						if ns=="+":
							y=y+1
						elif ns=="-":
							y=y-1
						elif ns=="":
							y=y+1
						else:
							y=y+float(ns)
						ns=""
					elif letra =="z":
						if ns=="+":
							z=z+1
						elif ns=="-":
							z=z-1
						elif ns=="":
							z=z+1
						else:
							z=z+float(ns)
						ns=""
					elif letra=="=":
						nb=True
						ns=""
					else:
						ns=ns+letra
				else:
					ns=ns+letra
			n=float(ns)
			self.fila.append(x)
			self.fila.append(y)
			self.fila.append(z)
			self.fila.append(n)
			self.matriz.append(self.fila)
		print "la Matriz Aumentada es la siguiente:"
		for x in self.matriz:
			print x
	def pedirCadena(self,i):
		cadena=raw_input("Profavor ingresar la ecuacion No. "+str(i+1)+"\n")
		return cadena