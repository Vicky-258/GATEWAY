from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import PasswordCheck

connection = sqlite3.connect('sorgavasal.db')
cursor = connection.cursor()

userName = ""
password = ""

userEntry = None
passEntry = None


def add_user():
    user = list(cursor.execute(f"""SELECT * FROM user_logins WHERE username = ('{userName}');"""))
    connection.commit()
    try:
        if userName == user[0][0]:
            messagebox.showerror("Error", "Username already exists")
    except IndexError:
        cursor.execute(f"""INSERT INTO user_logins(username,password) VALUES ('{userName}','{password}');""")
        connection.commit()
        messagebox.showinfo("Success", "User added")


def click():
    global userName, password
    userName = userEntry.get()
    password = passEntry.get()

    if PasswordCheck.check_password(password) == "lenerror":
        messagebox.showerror("Error", "Password should be at least 8 characters")
    elif PasswordCheck.check_password(password) == "charerror":
        messagebox.showerror("Error", "Password should contain only one character")
    elif PasswordCheck.check_password(password):
        add_user()
    else:
        messagebox.showerror("Error", "Weak Password")


def Add_main():
    global userEntry, passEntry
    window = Tk()

    window.geometry('500x500')
    window.title('Add User')
    window.resizable(False, False)
    window.config(padx=5, pady=5, bg='#1e1f22', relief='sunken')

    title = Label(window, text="Add User", bg='#1e1f22', fg='white', font=('Helvetica', 20, 'bold'))
    title.pack()

    seperator = ttk.Separator(window, orient=HORIZONTAL)
    seperator.place(y=50, height=3, width=500)

    userLabel = Label(window, text='User Name', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22', borderwidth=0,
                      relief='sunken')
    userLabel.place(x=95, y=100)

    passLabel = Label(window, text='Password', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22', borderwidth=0,
                      relief='sunken')
    passLabel.place(x=95, y=145)

    userEntry = Entry(window, font=("Arial", 10))
    userEntry.place(x=185, y=99, height=22.5, width=150)

    passEntry = Entry(window, font=("Arial", 10))
    passEntry.place(x=185, y=144, height=22.5, width=150)

    button = Button(window, text="Add user", bg="red", fg="white", command=click)
    button.place(x=200, y=190)

    window.mainloop()
