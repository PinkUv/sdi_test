from tkinter import *
from tkinter import ttk

def get_data(box):
    return box.get()

#Initializes root
root = Tk()
root.geometry("200x115")
root.resizable(False, False)
root.title("Gamma Login")

content = ttk.Frame(root)

#Variables
userlbl = ttk.Label(content, text="Username")
user = ttk.Entry(content)

passlbl = ttk.Label(content, text="Password")
passwd = ttk.Entry(content, show="*")

def CheckLogin():
    if (get_data(user) == "admin" and get_data(passwd) == "abc123"):
        print("Success")
    else:
        print("Incorrect username or password!")

loginbtn = ttk.Button(content, text="Login", command=CheckLogin)

#Positioning
content.pack()
userlbl.pack()
user.pack()
passlbl.pack()
passwd.pack()
loginbtn.pack()

root.mainloop()





