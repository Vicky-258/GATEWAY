from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import validation
import sqlite3

con = sqlite3.connect('sorgavasal.db')
c = con.cursor()


def list_user():
    rows = validation.list_user_details()

    # Display data in a Tkinter window
    lu = Tk()
    lu.title("Data from Database")

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
    style.configure('Treeview.Heading', background="green3")
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

    lu.resizable(width=False, height=False)
    lu.geometry("500x500")
    lu.config(background="#1e1f22")

    # Create a Treeview widget to display data in a tabular format
    tree = ttk.Treeview(lu, columns=("Username", "Password"), style="mystyle.Treeview", height=100)

    tree.heading("#0", text="Index")  # Index column
    tree.column("#0",width=162, anchor=CENTER)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=162, anchor=CENTER)

    # Insert data into Treeview
    for i, row in enumerate(rows, start=1):
        tree.insert("", "end", text=str(i), values=row, tags=('Username', 'Password'))

    tree.tag_configure("Username", background="#1e1f22", foreground="#ced0d6")
    tree.tag_configure("Password", background="#1e1f22", foreground="#ced0d6")

    tree.pack(expand=True, fill="both")

    lu.mainloop()

