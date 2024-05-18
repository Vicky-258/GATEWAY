from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect('sorgavasal.db')
cursor = connection.cursor()

username = ""
password = ""

userEntry = None
passEntry = None


def admin_remove():
    user = list(cursor.execute(f"SELECT * FROM user_logins WHERE username = ('{username}');"))
    connection.commit()
    try:
        if username == user[0][0]:
            cursor.execute(f"DELETE FROM user_logins WHERE username = ('{username}');")
            connection.commit()
            messagebox.showinfo("User Removed", "User Removed Successfully")
    except Exception:
        messagebox.showerror("Error", "Username does not exist")


def click():
    global username, password
    username = userEntry.get()
    password = passEntry.get()
    admin_remove()


def remove_main():
    global userEntry, passEntry

    window = Tk()
    window.geometry('500x500')
    window.title('Remove User')
    window.resizable(False, False)
    window.config(padx=5, pady=5, bg='#1e1f22', relief='sunken')

    title = Label(window, text="Remove User", bg='#1e1f22', fg='white', font=('Helvetica', 20, 'bold'))
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

    button = Button(window, text="Remove user", bg="red", fg="white", command=click)
    button.place(x=200, y=190)

    window.mainloop()

