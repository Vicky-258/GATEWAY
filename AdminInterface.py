from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Adminfunctions import Admin_functions_main
import sqlite3

connection = sqlite3.connect('sorgavasal.db')
cursor = connection.cursor()

userName = ""
password = ""

userEntry = None
passEntry = None


def Admin_login_main():
    global userEntry, passEntry

    def click():
        global userName, password
        userName = userEntry.get()
        password = passEntry.get()
        admin_check()

    def admin_check():
        admin_user = list(cursor.execute(f"""SELECT username FROM admin_login WHERE username = ('{userName}');"""))
        admin_pass = list(cursor.execute(f"""SELECT password FROM admin_login WHERE password = ('{password}');"""))
        connection.commit()
        try:
            if userName == admin_user[0][0] and password == admin_pass[0][0]:
                Admin_login_window.destroy()
                Admin_functions_main()

        except IndexError:
            messagebox.showinfo("Admin ", "Admin login failed")

    Admin_login_window = Tk()

    Admin_login_window.geometry('500x500')
    Admin_login_window.resizable(False, False)

    Admin_login_window.title('Admin Page')

    Admin_login_window.config(padx=0, pady=10, background='#1e1f22')

    title = Label(Admin_login_window, text="Admin Login", font=("Helvetica", 20), fg="#ced0d6", bg="#1e1f22")
    title.pack()

    seperator = ttk.Separator(Admin_login_window, orient=HORIZONTAL)
    seperator.place(y=50, height=3, width=500)

    userLabel = Label(Admin_login_window, text='User Name', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                      borderwidth=0,
                      relief='sunken')
    userLabel.place(x=95, y=100)

    passLabel = Label(Admin_login_window, text='Password', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                      borderwidth=0,
                      relief='sunken')
    passLabel.place(x=95, y=145)

    button = Button(Admin_login_window, text="log in", bg="red", fg="white", command=lambda: click())
    button.place(x=200, y=190)

    userEntry = Entry(Admin_login_window, font=("Arial", 10))
    userEntry.place(x=185, y=99, height=22.5, width=150)

    passEntry = Entry(Admin_login_window, font=("Arial", 10), show='*')
    passEntry.place(x=185, y=144, height=22.5, width=150)

    Admin_login_window.mainloop()
