from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import PasswordCheck

connection = sqlite3.connect('sorgavasal.db')
cursor = connection.cursor()

username = ""
password = ""

new_name = ""
new_pass = ""

userEntry = None
passEntry = None
NewuserEntry = None
NewpassEntry = None


def admin_edit():
    user = list(cursor.execute(f"""SELECT * FROM user_logins WHERE username = ('{username}');"""))
    pa_ss = list(cursor.execute(f"""SELECT * FROM user_logins WHERE password = ('{password}');"""))
    connection.commit()

    try:
        if username == user[0][0] and password == pa_ss[0][0]:
            cursor.execute(f"""UPDATE user_logins SET username = ('{new_name}');""")
            cursor.execute(f"""UPDATE user_logins SET password = ('{new_pass}');""")
            connection.commit()
    except IndexError:
        messagebox.showerror("Error", "Username or Password is incorrect")


def click():
    global userEntry, passEntry, NewuserEntry, NewpassEntry, username, password
    username = userEntry.get()
    password = passEntry.get()
    NewuserEntry = NewuserEntry.get()
    NewpassEntry = NewpassEntry.get()

    if PasswordCheck.check_password(NewpassEntry) == "lenerror":
        messagebox.showerror("Error", "Password should be at least 8 characters")
    elif PasswordCheck.check_password(NewpassEntry) == "charerror":
        messagebox.showerror("Error", "Password should contain only one character")
    elif PasswordCheck.check_password(NewpassEntry):
        admin_edit()
    else:
        messagebox.showerror("Error", "Weak Password")


def Edit_main():
    global userEntry, passEntry, NewuserEntry, NewpassEntry, username, password
    window = Tk()
    window.geometry('500x500')
    window.title('Edit User')
    window.resizable(False, False)
    window.config(padx=5, pady=5, bg='#1e1f22', relief='sunken')

    title = Label(window, text="Edit User", bg='#1e1f22', fg='white', font=('Helvetica', 20, 'bold'))
    title.pack()

    seperator = ttk.Separator(window, orient=HORIZONTAL)
    seperator.place(y=50, height=3, width=500)

    userLabel = Label(window, text='Old User Name', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                      borderwidth=0,
                      relief='sunken')
    userLabel.place(x=85, y=100)

    passLabel = Label(window, text='Old Password', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                      borderwidth=0,
                      relief='sunken')
    passLabel.place(x=85, y=145)

    userLabel = Label(window, text='New User Name', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                      borderwidth=0,
                      relief='sunken')
    userLabel.place(x=85, y=190)

    passLabel = Label(window, text='New Password', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                      borderwidth=0,
                      relief='sunken')
    passLabel.place(x=85, y=235)

    userEntry = Entry(window, font=("Arial", 10))
    userEntry.place(x=185, y=99, height=22.5, width=150)

    passEntry = Entry(window, font=("Arial", 10), show="*")
    passEntry.place(x=185, y=144, height=22.5, width=150)

    NewuserEntry = Entry(window, font=("Arial", 10))
    NewuserEntry.place(x=185, y=189, height=22.5, width=150)

    NewpassEntry = Entry(window, font=("Arial", 10), show="*")
    NewpassEntry.place(x=185, y=238, height=22.5, width=150)

    button = Button(window, text="Edit user", bg="red", fg="white", command=click)
    button.place(x=200, y=283)

    window.mainloop()
