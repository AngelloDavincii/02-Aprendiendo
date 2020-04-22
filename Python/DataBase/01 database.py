import sqlite3

miConexion = sqlite3.connect("FirstDataBase")


miCursor = miConexion.cursor()

#Se crea tabla
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(30))")
#Se inserta registro
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

'''
variosProductos=[

	("Camiseta","10","DEPORTES"),
	("Jarron",90,"CERAMICA"),
	("Cammion",20,"JUGUETERIA")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
'''
miCursor.execute("SELECT * FROM PRODUCTOS")
#obtenemos la informacion de la tabla y lo mete a una lista
many = miCursor.fetchall()



for producto in many:
	print("Nombre Articulo: ", producto[0],"Seccion: ",producto[2])

miConexion.commit()

miConexion.close()