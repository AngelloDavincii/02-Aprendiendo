from tkinter import *

root = Tk()

root.title("Example")

playa = IntVar()
mountain = IntVar()
turismo = IntVar()

def travel():
	choice = ""

	if playa.get() == 1:
		choice+= " Has escogido la playa "
	if mountain.get() == 1:
		choice+= " Has escogido la montana "
	if turismo.get() == 1:
		choice+= " Has escogido turismo "

	final.config(text = choice)

foto = PhotoImage(file = "mario.png")
Label(root, image = foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text = "Elige destinos", width = "50").pack()

Checkbutton(root, text = "Playa", variable = playa, onvalue = 1, offvalue = 0, command = travel).pack()
Checkbutton(root, text = "Mountain", variable = mountain, onvalue = 1, offvalue = 0, command = travel).pack()
Checkbutton(root, text = "Turismo", variable = turismo, onvalue = 1, offvalue = 0, command = travel).pack()

final = Label(frame)
final.pack()


root.mainloop()