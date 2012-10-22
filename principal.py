from matrizTraspuesta import MatrizTraspuesta
from matrizInversa import MatrizInversa
from Sistema3x3 import Sistema3x3
from matrizAumentada import MatrizAumentada

class Principal(object):
	"""docstring for principal"""
	def __init__(self):
		r=0
		while(r!=5) :
			self.menu()
			r=int(raw_input("Cual seleccion escoge"))
			self.seleccion(r)

	def menu(self):
		print"="*42
		print"Bienvendios programa de Algebra lineal"
		print"--------Hecho en PYTHON---------------"
		print"1..........................Sistema 3x3"
		print"2.......................Matriz Inversa"
		print"3....................Matriz Traspuesta"
		print"4.....................Matriz Aumentada"
		print"5................................Salir"
	def seleccion(self,s):
		print"-"*10
		if s==1:
			print "-------Sistema 3x3--------------"
			sistema=Sistema3x3()
			sistema.calcular()
		elif s==2:
			print"--------MATRIZ INVERSA-----------"
			sistemaInverso= MatrizInversa()
			sistemaInverso.calcularM()
		elif s==3:
			print"-----MATRIZ TRASPUESTA-----------"
			sistemaTraspuesto = MatrizTraspuesta()
			sistemaTraspuesto.matrizinversa()
		elif s==4:
			print"------MATRIZ AUMENTADA----------"
			sistemaAumentado= MatrizAumentada()
			sistemaAumentado.procesar()
		elif s==5:
			print"gracias por usar el programa"
		else:
			print"error ingrese otra funcion"
		hs=raw_input("Presione enter para continuar")
p=Principal()		



		
		