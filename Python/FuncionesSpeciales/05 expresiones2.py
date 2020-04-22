import re

#Caracteres comodin
names = ['Ana Gomez',
			'Maria Martin',
			'Sandra Lopez',	
			'Santiago Martin']

# El "^" busca todos los objetos que comienza por algo
# en este caso por Sandra
for element in names:
	if re.findall('^Sandra',element):
		print(element)

# El "^" busca todos los objetos que termina por algo
# en este caso por Martin
for element in names:
	if re.findall('Martin$',element):
		print(element)
