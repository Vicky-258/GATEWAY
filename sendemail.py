from email.message import EmailMessage
import ssl
import smtplib
import generatecode as g


# call this function to test this code
def send_mail(userEmail):
    email_sender = 'gateauthenticator@gmail.com'
    email_password = 'pdeuzkiwvjexpkax'  # dont change this passkey
    # don't use this gzhlcwxcztsvxanq becoz this is old mail passkey
    email_reciver = userEmail

    subject = "GATE LOGIN VERIFICATION:"  # edit this when u need to change subject
    otp = g.generate_code()  # import generatecode.py to run this function

    body = f"Your OTP : {otp}\n\nDon't Share OTP with anyone for your privacy and security\n\nThank you for using GATE🥰"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['Subject'] = subject

    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())
        print('sent')
        return otp
    except:
        print('An Error Occured')
