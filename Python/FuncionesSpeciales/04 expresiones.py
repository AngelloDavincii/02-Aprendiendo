import re

cadena = "Vamos a aprender como programar en python Vamos"
cadena2 = "23213"
buscar = "Vamos"
#Nos dice en que posicion esta un objeto y si esta el objeto
print(re.search("aprender",cadena))

#
if re.search(buscar, cadena) is not None:
	print("Si lo encontre")


else:
	print("CHALE no esta")

#me devuelve una lista con las palabras que se repiten
print(re.findall(buscar,cadena))