from tkinter import *

root = Tk()

option = IntVar()

def printi():
	#print(option.get())
	if option.get() == 1:
		etiqueta.config(text = "has elegido masculino")

	elif option.get() == 2:
		etiqueta.config(text = "has elegido femenino")

	else:
		etiqueta.config(text = "Has elegido otros")

Label(root, text="Gender").pack()

Radiobutton(root,text = "Male",variable = option,value = 1,command=printi).pack()

Radiobutton(root,text = "Female",variable = option,value = 2,command=printi).pack()

Radiobutton(root,text = "Other",variable = option,value = 3,command=printi).pack()


etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
