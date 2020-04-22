import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#Primary key es para hacer que cada objeto sea unico
# para hacer que se gestiono solo el codigo de identificacion
# entonces le ponemos el autoincrement
# Unique hace que no se repita en algun lado dos elementos iguales
miCursor.execute('''
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos = [
	("pelota",20,"jugueteria"),
	("pantalon",15,"confeccion"),
	("destornillador",25,"ferreteria"),
	("jarron",45,"ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'jugueteria')")

miConexion.commit()

miConexion.close()