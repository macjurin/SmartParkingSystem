import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(email_send,body):
    email_user = "noreply.car.system@gmail.com"
    email_password = "Carparksystem1234"
    subject = "NAVIGATION"

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_send, text)
    server.quit()


