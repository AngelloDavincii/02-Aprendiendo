from tkinter import *

root = Tk()

miFrame = Frame(root,width=500, height = 400)
miFrame.pack()

image = PhotoImage(file = "mario.png")
#creando texto
frase = Label(miFrame, text = "Como estas PUTO",fg = "#9370DB", font=("Comic Sans MS",30))
#Nos permite colocar el text en coordenadas x y
Label(miFrame, image = image).place(x=100,y=100)
frase.place(x=100,y=100)

root.mainloop()