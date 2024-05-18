import time
from tkinter import *
from tkinter import ttk, messagebox
import generatecode
import sendemail

f = ("Arial", 10)

result = False

userEmail = input("Enter Your Email Address: ")


def otp_win(useremail):
    global result
    sent_otp = sendemail.send_mail(useremail)

    def otp_submit():
        global result
        user_otp = otpEntry.get()

        if user_otp == sent_otp:
            otp_veri = Label(otp_window, text="OTP verification successful", fg="#549159", bg="#1e1f22",
                             font=("Arial", 15))
            otp_veri.place(y=250, x=125)

            result = True
            print("OTP verification successful")

            otp_window.after(10000, otp_window.destroy())
        else:
            otp_unveri = Label(otp_window, text="OTP verification failed", fg="#b54747", bg="#1e1f22",
                               font=("Arial", 15))
            otp_unveri.place(y=250, x=125)
            result = False
            print("OTP verification failed")
            otp_window.after(10000, otp_window.destroy())

    otp_window = Tk()
    otp_window.geometry('500x500')
    otp_window.resizable(False, False)
    otp_window.title('OTP Verification')

    title = Label(otp_window, text='Verification Page', font=('Arial', 15), fg='#4f87f9', bg='#1e1f22')
    title.pack()

    seperator = ttk.Separator(otp_window, orient=HORIZONTAL)
    seperator.place(y=50, height=3, width=500)

    minute = StringVar()
    second = StringVar()

    minute.set("02")
    second.set("30")

    mins_tf = Label(
        otp_window,
        background='#1e1f22',
        foreground='#ced0d6',
        width=3,
        font=f,
        textvariable=minute)

    mins_tf.place(x=293, y=208)

    sec_tf = Label(
        otp_window,
        background='#1e1f22',
        foreground='#ced0d6',
        width=3,
        font=f,
        textvariable=second)

    sec_tf.place(x=313, y=208)

    resend = Button(otp_window,
                    text='Resend OTP',
                    font=f,
                    bg='#1e1f22',
                    fg='#ced0d6',
                    activeforeground='#ced0d6',
                    activebackground='#1e1f22',
                    borderwidth=0,
                    relief='flat',
                    )

    resend.place(x=280, y=180)

    def startCountdown():
        userinput = 150
        while userinput > -1:
            mins, secs = divmod(userinput, 60)

            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            otp_window.update()
            otp_window.after(1000)

            userinput -= 1
        return userinput

    otp_window.config(padx=0, pady=10, background='#1e1f22', relief='sunken')

    otpLabel = Label(otp_window, text='Enter the OTP', font=('Arial', 10, 'italic'), fg='#ced0d6', bg='#1e1f22',
                     borderwidth=0,
                     relief='sunken')
    otpLabel.place(x=90, y=130)

    otpEntry = Entry(otp_window, font=("Arial", 10))
    otpEntry.place(x=185, y=129, height=22.5, width=150)

    button = Button(otp_window, text="Submit", bg="red", fg="white", command=lambda: otp_submit())
    button.place(x=215, y=180)

    if startCountdown() == -1:
        messagebox.showinfo("OTP Verification", "OTP verification unsuccessful")
        otp_window.after(1000, lambda: otp_window.destroy())
    otp_window.mainloop()

