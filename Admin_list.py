from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
connection = sqlite3.connect('sorgavasal.db')
cursor = connection.cursor()

def List_main():
    global records
    try:
       queries = """SELECT username FROM user_logins"""
       cursor.execute(queries)
       records = cursor.fetchall()

    except Exception:
        messagebox.showerror("Error", "Database Error")
    window = Tk()
    window.geometry('500x500')
    window.title('list of Users')
    window.resizable(False, False)
    window.config(padx=5, pady=5, bg='#1e1f22', relief='sunken')

    title = Label(window, text="All Users", bg='#1e1f22', fg='white', font=('Helvetica', 20, 'bold'))
    title.pack()

    seperator = ttk.Separator(window, orient=HORIZONTAL)
    seperator.place(y=50, height=3, width=500)

    t = Text(window, font=('Helvetica', 15, 'bold'), bg='#1e1f22', fg='white', borderwidth=0, relief='sunken')
    for x in list(records):
        t.insert(END,f" =>  {x[0]}\n\n")
    t.place(x=0, y=75)

    window.mainloop()
