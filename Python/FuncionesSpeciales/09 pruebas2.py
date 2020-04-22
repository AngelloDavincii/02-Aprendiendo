import math

lista = [1,4,9,19]

def raizCuadrada(goku):
	"""
	La funcion devuelve una lista con la raiz cuadrada
	de los elementos numericos pasados por parametros
	en otra lista

	>>> lista2 = []
	>>> for i in lista:
	... 	lista2.append(i)
	>>> raizCuadrada(lista2)
	[1.0,2.0,3.0,4.0]

	"""


	return [math.sqrt(n) for n in goku]

print (raizCuadrada(lista))


import doctest
doctest.testmod()