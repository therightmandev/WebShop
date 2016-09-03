import smtplib
from .. import EMAIL, EMAIL_PASSWORD


def send_verification_email(email):
    """this is supposed to send a verfication email
    BUT at the moment it only sends a 'welcome' email"""
    print(type(email))
    print(type(EMAIL))
    print(type(EMAIL_PASSWORD))
    msg = 'Hey hey!'
    username = EMAIL
    password = EMAIL_PASSWORD
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(EMAIL, email, msg)
    server.quit()
 
