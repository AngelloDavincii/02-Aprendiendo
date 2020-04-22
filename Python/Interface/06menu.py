from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
#Aviso sin nada
def info():
	messagebox.showinfo("Esto es un aviso del Procesador", "Procesador de textos version 2018")
#warning message
def license():
	messagebox.showwarning("Licence","Product under licence 2020")
#question message Si o No
def leave():
	value = messagebox.askokcancel("Salir","You wish leave the application?")
	#esto termina con el programa
	if value == True:
		root.destroy()
#Reintentar o cancelar
def close():
	value = messagebox.askokcancel("Reintentar","No es posible cerrar")


def abrir():
	file = filedialog.askopenfilename(title = "Abrir", initialdir = "D:", filetypes = (("Archivos de Excel","*.xlsx"),("Archivos de texto", ".*txt"),("Todos los ficheros","*.*")))

barraMenu = Menu(root)
root.config(menu = barraMenu, width=300,height=300)

archivoMenu=Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "New")
archivoMenu.add_command(label = "Save")
archivoMenu.add_command(label = "Save ass")
archivoMenu.add_command(label = "Open", command = abrir)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Close", command = close)
archivoMenu.add_command(label = "Quit", command = leave)

archivoEdicion=Menu(barraMenu, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoHerramientas=Menu(barraMenu, tearoff = 0)

archivoHelp=Menu(barraMenu, tearoff = 0)
archivoHelp.add_command(label = "Licencia", command = license)
archivoHelp.add_command(label = "About it...", command = info)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edicion", menu = archivoEdicion)
barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)
barraMenu.add_cascade(label = "Help", menu = archivoHelp)

root.mainloop()