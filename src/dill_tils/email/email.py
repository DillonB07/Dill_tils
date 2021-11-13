import os
import smtplib
from email.message import EmailMessage


class Email:
    """Connect to SMTP server and send emails"""

    def __init__(self, recipient: str, sender: str, password: str = os.environ['PASSWORD'], server: str = 'smtp.yandex.com', port: int = 465):
        """
        Connect to SMTP server and set variables for Email class
        """
        self.recipient = recipient
        self.sender = sender
        self.server = smtplib.SMTP_SSL(server, port)
        self.server.login(self.sender, password)
        print('Connected')

    def sendEmail(self, subject, message):
        """Send an email using variables in self"""
        email = f'Name: {self.name}\nEmail: {self.email}\nSubject: {self.subject}\nMessage: {message}'
        msg = EmailMessage()
        msg.set_content(email)
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = self.recipient
        try:
            self.server.send_message(msg)
            print('Email successfully sent')
            return True
        except Exception as e:
            print(e)
            return False
