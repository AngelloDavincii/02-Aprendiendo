def area(lado):
	"""
	ESTO HACE QUE TU MAMA...
	"""
	return "El area de un cuadrado es "+ str(lado*lado)

def areaT(base,altura):
	return "El area del triangulo es: "+ str((base*altura)/2)

print(area(2))

print(area.__doc__)

lista = [2,3,4]

help(lista)