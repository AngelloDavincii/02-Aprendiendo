import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#para hacer un cambio en algun registro
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO='pelota'")

#OJO con el where para borrar
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

miConexion.commit()

miConexion.close()