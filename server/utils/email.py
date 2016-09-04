import smtplib, socket
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
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        try:
            server.login(username,password)
        except smtplib.SMTPAuthenticationError:
            sys.exit('Email and/or password in server/config.py is incorrect')
        server.sendmail(EMAIL, email, msg)
        server.quit()
        return (True,)
    except socket.gaierror as s:
        print('SOCKET ERROR!', s)
        return (False, 'socket')
 
