from tkinter import *
from tkinter import messagebox as tmsg
import solver
import time 
import requests


root = Tk()
root.geometry("700x700+380+70")

############### IMAGES
bgimg = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//board.png")
submit = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//submit2.png")
rs = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//restart.png")
#############


label1 = Label(root,image = bgimg)
label1.place(relx=0, rely=0, width=700, height=700)


#api call

try :
	api_board = requests.get("http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9/&level=2")
	api_board = api_board.json()
except:
	tmsg.showerror("Error","No Internet Connection !")
	root.destroy()


example_board= [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],
				[-1,-1,-1,-1,-1,-1,-1,-1,-1],]


#print(api_board['squares'])
for option in api_board['squares']:
	example_board[ option["x"] ][ option["y"] ] = option['value'] 

entry_list = []

################ CONSTANTS
VALX_ = 0.063
VALY_ = 0.154
###############


def callback( P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


#for creating the entries
for i in range(9):
	for j in range(9):
		vcmd = (root.register(callback))
		test = Entry(root,font=70,validate='all', validatecommand=(vcmd, '%P'))
		
		test.place(relx=VALX_, rely=VALY_, width=40, height=38)
		entry_list.append(test)
		VALX_ += 0.065
	VALY_ += 0.065
	VALX_ = 0.063


#for placing the numbers
count  = 0
for i in range(9):
	for j in range(9):
		#print(example_board[i][j],entry_list[count])
		if example_board[i][j] != -1:
			entry_list[count].insert(0,str(example_board[i][j]))
			entry_list[count].config(state='disabled',disabledbackground="cyan",disabledforeground="black")
		count+=1


def check_if_won():
	solved_version = solver.solve_for_game()
	count = 0
	flag =0 
	for i in range(9):
		for j in range(9):
			#entry_list[count].config(state='normal')
			if len(str(entry_list[count].get())) != 1:
				flag = 2
				break
			if str(entry_list[count].get()) != str(solved_version[i][j]):
				flag = 1
				break
			else:
				print("Yes")
			count+=1
		if flag == 1:
			break
		if flag == 2:
			break

	if flag == 1:
		tmsg.showerror("ERROR")
	elif flag == 2:
		tmsg.showerror("Error","You shall submit after filling every entry !")
	else :
		tmsg.showinfo("WIN")


def restart_game():
	if not tmsg.askyesno("Restart?","All tracked entries will be lost !"):
		return

	count = 0
	for i in range(9):
		for j in range(9):
			if entry_list[count]['state'] != 'disabled':
				entry_list[count].delete(0,"end")
			count+=1


submit_ = Button(root,command = check_if_won,image = submit)
submit_.place(relx=0.2, rely=0.8,width=160, height=80)
submit_.configure(relief="flat")
submit_.configure(overrelief="flat")
submit_.configure(activebackground="#ffde59")
submit_.configure(cursor="hand2")
submit_.configure(borderwidth="0")

restart = Button(root,command = restart_game,image = rs)
restart.place(relx=0.6, rely=0.8,width=160, height=80)
restart.configure(relief="flat")
restart.configure(overrelief="flat")
restart.configure(activebackground="#ffde59")
restart.configure(cursor="hand2")
restart.configure(borderwidth="0")

root.mainloop()
