from tkinter import *
from tkinter import ttk
import Admin_add
import Admin_edit
import Admin_remove
import list


def Admin_functions_main():
    def add():
        Admin_add.Add_main()

    def edit():
        Admin_edit.Edit_main()

    def remove():
        Admin_remove.remove_main()

    def listUsers():
        list.list_user()

    Admin_functions_window = Tk()
    Admin_functions_window.title("Admin Interface")
    Admin_functions_window.geometry("500x500")
    Admin_functions_window.configure(padx=5, pady=5, bg="#1e1f22", relief="sunken")
    Admin_functions_window.resizable(width=False, height=False)

    Admin_functions_title = Label(Admin_functions_window, text="Admin Interface", bg='#1e1f22', fg='white',
                                  font=('Helvetica', 20, 'bold'))
    Admin_functions_title.pack()

    Admin_functions_seperator = ttk.Separator(Admin_functions_window, orient=HORIZONTAL)
    Admin_functions_seperator.place(y=50, height=3, width=500)

    add_img = PhotoImage(file="add.png")
    remove_img = PhotoImage(file="remove.png")
    edit_img = PhotoImage(file="edit.png")
    list_img = PhotoImage(file="list.png")

    Add_btn = Button(
        Admin_functions_window,
        image=add_img,
        bg='#1e1f22',
        borderwidth=0,
        relief="sunken",
        activebackground="#1e1f22",
        width=100,
        height=100,
        command=add,
    )
    Add_btn.place(x=50, y=75)

    Add_label_btn = Button(Admin_functions_window,
                           text="Add User",
                           font=('Arial', 15),
                           borderwidth=0,
                           fg='#4f87f9',
                           bg='#1e1f22',
                           activebackground='#2b2d30',
                           activeforeground='#4f87f9',
                           command=lambda: add())
    Add_label_btn.place(x=49, y=167)

    remove_btn = Button(
        Admin_functions_window,
        image=remove_img,
        bg="#1e1f22",
        borderwidth=0,
        relief="sunken",
        activebackground="#1e1f22",
        height=100,
        width=100,
        command=remove
    )
    remove_btn.place(x=325, y=75)

    remove_label = Button(Admin_functions_window,
                          text="Remove User",
                          font=('Arial', 15),
                          borderwidth=0,
                          fg='#4f87f9',
                          bg='#1e1f22',
                          activebackground='#2b2d30',
                          activeforeground='#4f87f9',
                          command=lambda: remove())
    remove_label.place(x=314, y=167)

    edit_btn = Button(
        Admin_functions_window,
        image=edit_img,
        bg="#1e1f22",
        borderwidth=0,
        relief="sunken",
        activebackground="#1e1f22",
        height=100,
        width=100,
        command=edit
    )
    edit_btn.place(x=50, y=275)

    edit_label = Button(Admin_functions_window,
                        text="Edit User",
                        font=('Arial', 15),
                        borderwidth=0,
                        fg='#4f87f9',
                        bg='#1e1f22',
                        activebackground='#2b2d30',
                        activeforeground='#4f87f9',
                        command=lambda: edit())
    edit_label.place(x=56, y=369)

    list_btn = Button(
        image=list_img,
        bg="#1e1f22",
        borderwidth=0,
        relief="sunken",
        activebackground="#1e1f22",
        width=100,
        height=100,
        command=listUsers
    )
    list_btn.place(x=314, y=275)

    edit_label = Button(Admin_functions_window,
                        text="List Users",
                        font=('Arial', 15),
                        borderwidth=0,
                        fg='#4f87f9',
                        bg='#1e1f22',
                        activebackground='#2b2d30',
                        activeforeground='#4f87f9',
                        command=lambda: listUsers())
    edit_label.place(x=321, y=369)

    Admin_functions_window.mainloop()
