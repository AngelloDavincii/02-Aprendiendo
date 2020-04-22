from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")
#Esto hace que no sea resizable la ventana
#raiz.resizable(0,0)
#se le cambia icono a la ventana
raiz.iconbitmap("mar.ico")
#tamano de la ventana
raiz.geometry("300x300")
#background color
raiz.config(bg="#EEE8AA")
#Configurando un widget
miFrame = Frame()
#se empaqueta, side and anchor le dice la posicion al frame
#Con fill and expand podemos hacer que el frame se expanda 
#con la ventana both para modificar de todos lados y y para el eje y
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="200", height = ("200"))
#para cambiar el borde se usa relief
#para borde se usa bd
#para cambiar la flecha sobre icono cursor
miFrame.config(bd = 35,relief = "groove", cursor = "hand1")



raiz.mainloop()