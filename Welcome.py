from tkinter import *
from AdminInterface import Admin_login_main
import Interface

window = Tk()

window.geometry('500x500')
window.resizable(False, False)

window.title('Welcome')

title = Label(window, text='Welcome to GATE', font=('Arial', 15), fg='#4f87f9', bg='#1e1f22')
title.pack()

window.config(padx=0, pady=10, background='#1e1f22', relief='sunken')


def Welcome_main():
    def Admin():
        window.destroy()
        Admin_login_main()

    def user():
        window.destroy()
        Interface.User_login_main()

    photo = PhotoImage(file='person_24dp_FILL0_wght400_GRAD0_opsz24.png')

    Admin_btn = Button(
        image=photo,
        bg='#2b2d30',
        borderwidth=0,
        relief='sunken',
        activebackground='#2b2d30',
        command=lambda: Admin()
    )
    Admin_btn.place(x=200, y=50)

    Admin_name_btn = Button(window,
                            text="Admin Login",
                            font=('Arial', 15),
                            borderwidth=0,
                            fg='#4f87f9',
                            bg='#1e1f22',
                            activebackground='#2b2d30',
                            activeforeground='#4f87f9',
                            command=lambda: Admin())
    Admin_name_btn.place(x=195, y=160)

    photo2 = PhotoImage(file='group_24dp_FILL0_wght400_GRAD0_opsz24.png')

    user_btn = Button(
        image=photo2,
        bg='#2b2d30',
        borderwidth=0,
        relief='sunken',
        activebackground='#2b2d30',
        command=lambda: user()
    )
    user_btn.place(x=200, y=230)

    user_name_btn = Button(window,
                           text="User Login",
                           font=('Arial', 15),
                           borderwidth=0,
                           fg='#4f87f9',
                           bg='#1e1f22',
                           activebackground='#2b2d30',
                           activeforeground='#4f87f9',
                           command=lambda: user())
    user_name_btn.place(x=195, y=340)

    window.mainloop()


Welcome_main()
