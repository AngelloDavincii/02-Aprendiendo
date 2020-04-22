from tkinter import *
from tkinter import filedialog


root = Tk()

def abrir():
	file = filedialog.askopenfilename(title = "Abrir", initialdir = "D:", filetypes = (("Archivos de Excel","*.xlsx"),("Archivos de texto", ".*txt"),("Todos los ficheros","*.*")))

Button (root, text = "Open File", command = abrir).pack()


root.mainloop()