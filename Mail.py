
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


fromaddr = 'josef.kirsh01@gmail.com'
toaddrs  = 'josef.kirsh01@gmail.com'
# msg = 'There was a terrible error that occured and I wanted you to know!'


def Send_mail(msg):
    # Credentials (if needed)
    username = 'josef.kirsh01'
    password = 'Diana1234@'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    username = 'josef.kirsh01'
    password = 'Diana1234@'
    """this is some test documentation in the function"""
    message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.starttls()
    server.login(username, password)
    server.sendmail(FROM, TO, message)
    server.quit()

def sendSmartEmail():
    recipients = ['rcpt1@example.com', 'rcpt2@example.com', 'group1@example.com']
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = str(sys.argv[1])
    msg['From'] = 'abcxyz@gmail.com'
    msg['Reply-to'] = 'abcxyz@gmail.com'

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText("Hi, please find the attached file")
    msg.attach(part)

    part = MIMEApplication(open(str(sys.argv[2]), "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
    msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("abcxyz@gmail.com", "yourpasswordhere")

    server.sendmail(msg['From'], emaillist, msg.as_string())


# ######################## Main ########################
if __name__ == '__main__':
    sendMail(fromaddr, toaddrs, 'Test Header', 'test msg', 'smtp.gmail.com:587')
