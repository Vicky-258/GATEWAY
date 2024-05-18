from tkinter import *


window = Tk()
window.geometry('500x500')
window.resizable(False, False)
window.title('OTP Verification')

title = Label(window, text='Verification Page', font=('Arial', 15), fg='#4f87f9', bg='#1e1f22')
title.pack()

window.config(padx=0, pady=10, background='#1e1f22', relief='sunken')


otpLabel = Label(window, text='OTP', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22', borderwidth=0,
                      relief='sunken')
otpLabel.place(x=150, y=105)

otpEntry = Entry(window, font=("Arial", 10))
otpEntry.place(x=185, y=99, height=22.5, width=150)

button = Button(window, text="Submit", bg="red", fg="white")
button.place(x=215, y=130)


window.mainloop()