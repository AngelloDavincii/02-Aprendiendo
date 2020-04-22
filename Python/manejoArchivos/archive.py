from io import open

archivo_texto = open("archivo.txt","r")

lines = archivo_texto.readlines()

archivo_texto.close()

print(lines)
#Para escribir sobre un archivo de texto
#puto = "maravillosamente estupido estimado imbecil"

#archivo_texto.write(puto)

#archivo_texto.close()
