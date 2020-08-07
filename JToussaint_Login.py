#Login
from tkinter import *
import os
import re

def delete2():
	screen3.destroy()

def delete3():
	screen4.destroy()

def delete4():
	screen5.destroy()

def login_success():
	global screen3
	screen3 = Toplevel(screen)
	screen3.title("Success")
	screen3.geometry("150x100")
	Label(screen3, text = "Login Success").pack()
	Button(screen3, text = "OK", command = delete2).pack()

def password_not_recognize():
	global screen4
	screen4 = Toplevel(screen)
	screen4.title("Success")
	screen4.geometry("150x100")
	Label(screen4, text = "Password Not Recognized").pack()
	Button(screen4, text = "OK", command = delete3).pack()
 
def password_not_found():
	global screen5
	screen5 = Toplevel(screen)
	screen5.title("Success")
	screen5.geometry("150x100")
	Label(screen5, text = "User not Found").pack()
	Button(screen5, text = "OK", command = delete4).pack()

def register_user():
	username_info = username.get()
	password_info = password.get()

	file = open(username_info, "w")
	file.write(username_info+"\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(screen1, text = "Registration Success", fg = "green", font = ("calibri", 11)).pack()

def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	username_entry1.delete(0, END)
	password_entry1.delete(0, END)

	list_of_files = os.listdir()
	if username1 in list_of_files:
		file1 = open(username1, "r")
		#read the text  in files and split them where there a space
		verify = file1.read().splitlines() 
		#check to see if the password a verify password
		if password1 in verify:
			login_success()
		else:
			password_not_recognize()
	else:
		password_not_found()

def register():
	global screen1
	global username
	global password
	global username_entry
	global password_entry

	screen1 = Toplevel(screen)
	screen1.title("Register")
	screen1.geometry("300x250")
	
	username = StringVar()
	password = StringVar()

	Label (screen1, text = "Please Enter Details Below").pack()
	Label (screen1, text = "").pack()

	Label (screen1, text = "Username * ").pack()
	username_entry = Entry (screen1, textvariable = username)
	username_entry.pack()

	Label (screen1, text = "Password * ").pack()
	password_entry = Entry (screen1, textvariable = password)
	password_entry.pack()

	Label (screen1, text = "").pack()
	Button (screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

	p = password_info

	x = True	
	while x:  
		if (len(p) <6 or len(p) > 20):
			Label (screen1, text= "Password is Too Short.", fg = "red", font = ("calibri", 11)).pack()
			break
		elif not re.search("[a-z]",p):
			Label (screen1, text= "Password must have at least 1 lowercase letter.", fg = "red", font = ("calibri", 11)).pack()
			break
		elif not re.search("[0-9]",p):
			Label (screen1, text= "Password must have at least 1 number.", fg = "red", font = ("calibri", 11)).pack()
			break
		elif not re.search("[A-Z]",p):
			Label (screen1, text= "Password must have at least 1 uppercase letter.", fg = "red", font = ("calibri", 11)).pack()
			break
		else:
			#print("Valid Password")
			Label (screen1, text= "Valid Password", fg = "green", font = ("calibri", 11)).pack()		
			x = False
			break 

def login():
	global screen2
	global username_verify
	global password_verify
	global username_entry1
	global password_entry1

	screen2 = Toplevel(screen)
	screen2.title("Login")
	screen2.geometry("300x250")

	Label (screen2, text = "Please Enter Details Below to Login").pack()
	Label (screen2, text = "").pack()

	username_verify = StringVar()
	password_verify = StringVar()

	Label (screen2, text = "Username * ").pack()
	username_entry1 = Entry(screen2, textvariable = username_verify)
	username_entry1.pack()
	Label (screen2, text = "").pack()
	
	Label (screen2, text = "Password * ").pack()
	password_entry1 = Entry(screen2, textvariable = password_verify)
	password_entry1.pack()

	Label (screen2, text = "").pack()
	Button (screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
	global screen
	screen = Tk()
	screen.geometry("300x250")
	screen.title("Notes 1.0")
	Label1 = Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font =("calibri", 13)).pack()
	Label (text = "").pack()
	Button (text = "Login", height = "2", width = "30", command = login).pack()
	Label (text = "").pack()
	Button (text = "Register", height = "2", width = "30", command = register).pack()

	screen.mainloop()

main_screen()