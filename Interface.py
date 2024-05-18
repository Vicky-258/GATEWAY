from tkinter import *
import time
import sqlite3
from tkinter import ttk
from tkinter import messagebox

connection = sqlite3.connect('sorgavasal.db')
cursor = connection.cursor()

userName = ""
password = ""

userEntry = None
passwordEntry = None


def login_user():
    user = list(cursor.execute(f"""SELECT * FROM user_logins WHERE username = ('{userName}');"""))
    pa__ss = list(cursor.execute(f"""SELECT * FROM user_logins WHERE password = ('{password}');"""))
    connection.commit()

    try:
        if userName == user[0][0] and password == pa__ss[0][0]:
            messagebox.showinfo("User Login", "Login Successful")

    except IndexError:
        messagebox.showerror("User Login", "Login Failed")


def click():
    global userName, password
    userName = userEntry.get()
    password = passEntry.get()
    login_user()


def User_login_main():
    global userEntry, passEntry
    window = Tk()

    window.geometry('500x500')
    window.resizable(False, False)

    window.title('User Page')

    # icon = PhotoImage(file='icon.png')
    # window.iconphoto(True, icon)

    title = Label(window, text="Login Page", font=("Helvetica", 20), fg="#ced0d6", bg="#1e1f22")
    title.pack()

    seperator = ttk.Separator(window, orient=HORIZONTAL)
    seperator.place(y=50, height=3, width=500)

    userLabel = Label(window, text='User Name', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22', borderwidth=0,
                      relief='sunken')
    userLabel.place(x=95, y=100)

    passLabel = Label(window, text='Password', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22', borderwidth=0,
                      relief='sunken')
    passLabel.place(x=95, y=145)

    button = Button(window, text="log in", bg="red", fg="white", command=click)
    button.place(x=200, y=190)

    window.config(padx=0, pady=10, background='#1e1f22', relief='sunken')

    userEntry = Entry(window, font=("Arial", 10))
    userEntry.place(x=185, y=99, height=22.5, width=150)

    passEntry = Entry(window, font=("Arial", 10), show="*")
    passEntry.place(x=185, y=144, height=22.5, width=150)

    window.mainloop()
