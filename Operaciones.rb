class Operaciones
	#funciones para ingresar las dimensiones de la matriz
	def ingresoDeDimensionMatriz(mat)
		print "porfavor ingrese las dimensiones de la "+mat+" matriz" #pedir el inreso de la matriz
		b=false
		filas="a"
		columnas="a"
		@StDim=gets.chomp
 		@StDim.each_char {|a|
			if a=='x'
				b=true
				next
			end
			if b==true
				if filas=="a"
					filas=a
				else
					filas<<a
				end						
			elsif b==false
				if columnas=="a"
					columnas=a
				else
					columnas<<a
				end	
			end

			}
		@filas=filas.to_i
		@columnas=columnas.to_i
		puts @filas
		puts @columnas
	end
	def ingresoMatriz()
		a=1
		matriz=Array.new 
		fila=Array.new 
		for i in (0...@filas)
			for j in (1..@columnas)
				print "*"*5
				a=gets.chomp
				fila<<a
			end
			print"\n"
			matriz<<fila	
		end
		print matriz [0][1]
	end
end
operacion= Operaciones.new()
operacion.ingresoDeDimensionMatriz("primera")
operacion.ingresoMatriz()