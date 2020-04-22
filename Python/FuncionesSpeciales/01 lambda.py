def area(a,b):
	area = (b*a)/2
	return area

print(area(2,3))


resumen = lambda base,altura: (base*altura) / 2


print(resumen(2,3))

destacar = lambda comision: "!{}! Euros".format(comision)

valor = 120

print(destacar(valor))