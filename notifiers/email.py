import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(notification):
    mail_content = notification.message

    sender_address = os.environ.get('EMAIL_SENDER_ADDRESS')
    sender_pass = os.environ.get('EMAIL_SENDER_PASSWORD')
    receiver_address = os.environ.get('EMAIL_RECEIVER_ADDRESS')

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = notification.subject

    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
