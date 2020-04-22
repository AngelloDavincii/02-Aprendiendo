import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()
#con esto podemos filtrar
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confeccion'")


productos = miCursor.fetchall()

print(productos)

miConexion.commit()

miConexion.close()