from tkinter import *

root = Tk()
#creando cuadro de texto

square = Frame(root, width=500, height=600)
square.pack()

#sticky hace que los textos aparezcan alineados a un lado
#padx y pady es la distancia que hay entre el contenido
#con el contenedor
##########NOMBRE##############
minombre = StringVar()

nombre = Entry(square, text = minombre)
#Divide la interfaz en casillas
nombre.grid(row = 0, column = 1)

nameLabel = Label(square, text="Nombre: ")
nameLabel.grid(row = 0, column = 0, sticky = "w", pady = "10", padx = "10")

#########APELLIDO#############
apellido = Entry(square)
apellido.grid(row = 1, column = 1)

last = Label(square, text="Apellido: ")
last.grid(row = 1, column = 0, sticky = "w", pady = "10", padx = "10")
apellido.config(fg = "green")
#########DIRECCION#############
adress = Entry(square)
adress.grid(row = 2, column = 1)

direc = Label(square, text="Direccion de casa: ")
direc.grid(row = 2, column = 0, sticky = "w", pady = "10", padx = "10")

#########APELLIDO#############
password = Entry(square)
password.grid(row = 3, column = 1)

passi = Label(square, text="Password: ")
passi.grid(row = 3, column = 0, sticky = "w", pady = "10", padx = "10")

#########Comentarios#############
comentario= Text(square, width = 20, height = 6)
comentario.grid(row = 4, column = 1)

com = Label(square, text="Comments: ")
com.grid(row = 4, column = 0, sticky = "w", pady = "10", padx = "10")

#creando scrollbar
scroll = Scrollbar(square, command = comentario.yview)
scroll.grid(row = 4, column = 2, sticky = "nsew")

#funcion de relleno jaja
def codigo():
	print("Hola que tal, me alegra que me hayas escrito")
	print("Pense que ya no me recordabas, que te olvidaste de mi")
	minombre.set("TE QUIERO")
#boton
enviar = Button(root, text = "enviar", command = codigo)

enviar.pack()

root.mainloop()