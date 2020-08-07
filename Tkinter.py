#Login
from tkinter import *
 
def main_screen():
	screen = Tk()
	screen.geometry("300x250")
	screen.title("Notes 1.0")
	Label1 = Label(text = "Notes 1.0", bg = "grey", font =("Calibri", 13)).pack()
	Label1 (text = "").pack()
	Button (text = "Login").pack()
	Label1 (text = "").pack()
	Button (text = "Register").pack()
	
	screen.mainloop()

main_screen()