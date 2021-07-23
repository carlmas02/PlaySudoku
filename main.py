from tkinter import *
import os
 
root = Tk()
root.geometry("700x700+380+70")
 
 
def set_difficulty():
	new = Toplevel()
	new.geometry("500x250+460+200")

	def level(string):
		if string == "easy":
			new.destroy()
			root.withdraw()
			os.system("python game.py")
			root.deiconify()
			
		if string == "mid":
			print(1)
		if string == "hard":
			print(1)


	label1 = Label(new,image = imgdiff)
	label1.place(relx=0, rely=0, width=500, height=300)


	easy = Button(new,image = easybutton,command= lambda : level("easy"))
	mid = Button(new,image = midbutton,command= lambda : level("mid"))
	hard = Button(new,image = hardbutton,command= lambda : level("hard"))


	easy.configure(relief="flat")
	easy.configure(overrelief="flat")
	easy.configure(activebackground="#ffcab0")
	easy.configure(cursor="hand2")
	easy.configure(borderwidth="0")


	mid.configure(relief="flat")
	mid.configure(overrelief="flat")
	mid.configure(activebackground="#ffcab0")
	mid.configure(cursor="hand2")
	mid.configure(borderwidth="0")

	hard.place(relx=0.65, rely=0.73, width=160, height=80)
	hard.configure(relief="flat")
	hard.configure(overrelief="flat")
	hard.configure(activebackground="#ffcab0")
	hard.configure(cursor="hand2")
	hard.configure(borderwidth="0")

	easy.place(relx=0.02, rely=0.2,width=150, height=150)
	mid.place(relx=0.35, rely=0.2,width=150, height=150)
	hard.place(relx=0.67, rely=0.2,width=150, height=150)	


img = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//my2.png")
imgbutton = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//play.png")
imgdiff = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//diff2.png")
easybutton = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//easy.png")
midbutton = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//mid2.png")
hardbutton = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//hard.png")


label1 = Label(root,image = img)
label1.place(relx=0, rely=0, width=700, height=700)


button1 = Button(root,image = imgbutton)

button1.place(relx=0.65, rely=0.73, width=160, height=80)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffde59")
button1.configure(cursor="hand2")
button1.configure(borderwidth="0")
button1.configure(command = set_difficulty)


root.mainloop()
