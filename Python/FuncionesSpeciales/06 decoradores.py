#SUPER INTERESANTE
#*args dice que vamos a recibir un numero indefinido de parametros
#**kwargs 

#a una funcion se le puede pasar argumentos de tipo clave valor
#para hacer lo mismo que el *args se usa **kargs
def decorador(parametro):

	def funcion_interior(*args):
		# acciones adicionales que decoran
		print('Vamos a hacer un calculo')

		parametro(*args)

		# acciones adicionales que decoran

		print("Hemos terminado el calculo")

	return funcion_interior

@decorador
def suma(a,b):
	print(a + b)

@decorador
def resta(a,b):
	print(a - b)

#@decorador
def potencia(base, exponente):
	print(pow(base,exponente))

suma(15,20)
print()
resta(15,20)
print()
print(potencia(3,2))

