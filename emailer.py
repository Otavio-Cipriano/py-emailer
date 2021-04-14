import os
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

def send_email(body):
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv('EMAIL_SECRET')
    receiver_email = os.getenv('RECEIVER_EMAIL_SECRET')
    password = os.getenv('PASS_SECRET')

    message = MIMEMultipart("alternative")
    message["Subject"] = "Front End BR Vagas"
    message["From"] = sender_email
    message["To"] = receiver_email


    message_body = MIMEText(body, "plain")
    message.attach(message_body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )