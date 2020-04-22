from tkinter import *

root = Tk()

frame = Frame(root, width= 700, height = 700,background = "gray")
frame.pack()
#------------------PANTALLA--------------------------------------
var = StringVar()

pantalla = Entry(frame, textvariable = var)
pantalla.grid(row = 1, column =1, padx = 10, pady = 10, columnspan = 4)
pantalla.config(background = "black", fg = "#43F4A3", justify = "right")

operacion = ""
resultado = 0

#----------------PULSACIONES DEL TECLADO-----------------------
def selec(number):
	global operacion
	if operacion != "":
		var.set(number)
		operacion = ""

	else:
		var.set(var.get() + number)


def operar(ver, a):
	global operacion
	global resultado
	if ver == "suma":
		operacion = "+"
		resultado = resultado + int(a)
		var.set(resultado)
	if ver == "resta":
		operacion = "-"
		resultado = resultado - int(a)*-1
		var.set(resultado)
	if ver == "multi":
		operacion = "*"
		resultado = resultado * int(a)
		var.set(resultado)
	if ver == "division":
		operacion = "/"
		resultado = resultado / int(a)
		var.set(resultado)

def el_resultado():
	global resultado

	var.set(resultado + int(var.get()))
	resultado = 0


#-------------------FILAS------------------------------------
#funcion lambda hace que la funcion hasta que apachamos el boton
boton1 = Button(frame, text = "1", width=3, command = lambda:selec("1"))
boton1.grid(row = 2, column = 1)

boton2 = Button(frame, text = "2", width=3, command = lambda:selec("2"))
boton2.grid(row = 2, column = 2)

boton3 = Button(frame, text = "3", width=3, command = lambda:selec("3"))
boton3.grid(row = 2, column = 3)

botonx = Button(frame, text = "x", width=3, command = lambda:operar("multi",var.get()))
botonx.grid(row = 2, column = 4)

boton4 = Button(frame, text = "4", width=3, command = lambda:selec("4"))
boton4.grid(row = 3, column = 1)

boton5 = Button(frame, text = "5", width=3, command = lambda:selec("5"))
boton5.grid(row = 3, column = 2)

boton6 = Button(frame, text = "6", width=3, command = lambda:selec("6"))
boton6.grid(row = 3, column = 3)

botonD = Button(frame, text = "/", width=3, command = lambda:operar("division",var.get()))
botonD.grid(row = 3, column = 4)

boton7 = Button(frame, text = "7", width=3, command = lambda:selec("7"))
boton7.grid(row = 4, column = 1)

boton8 = Button(frame, text = "8", width=3, command = lambda:selec("8"))
boton8.grid(row = 4, column = 2)

boton9 = Button(frame, text = "9", width=3, command = lambda:selec("9"))
boton9.grid(row = 4, column = 3)

botonS = Button(frame, text = "+", width=3, command = lambda:operar("suma",var.get()))
botonS.grid(row = 4, column = 4)

boton0 = Button(frame, text = ".", width=3, command = lambda:selec("."))
boton0.grid(row = 5, column = 1)

boton0 = Button(frame, text = "0", width=3, command = lambda:selec("0"))
boton0.grid(row = 5, column = 2)

boton0 = Button(frame, text = "=", width=3, command = lambda:el_resultado())
boton0.grid(row = 5, column = 3)

botonI = Button(frame, text = "-", width=3, command = lambda:operar("resta",var.get()))
botonI.grid(row = 5, column = 4)

root.mainloop()