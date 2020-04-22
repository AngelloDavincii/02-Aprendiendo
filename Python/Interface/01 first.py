from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")
#Esto hace que no sea resizable la ventana
raiz.resizable(0,0)
#se le cambia icono a la ventana
raiz.iconbitmap("mar.ico")
#tamano de la ventana
raiz.geometry("300x300")
#background color
raiz.config(bg="#F08080")
raiz.mainloop()