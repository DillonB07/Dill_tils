import smtplib
from email.message import EmailMessage


class Email:
    """Connect to SMTP server and send emails

        Keyword arguments:
        recipient -- str: email address of recipient
        sender -- str: email address of sender
        password -- str: password of sender
        server -- str: SMTP server (default 'smtp.yandex.com')
        port -- int: SMTP port (default 465)

    """

    def __init__(self, recipient: str, sender: str, password: str, server: str = 'smtp.yandex.com', port: int = 465):
        """Connect to SMTP server and set self variables"""
        self.recipient = recipient
        self.sender = sender
        self.server = smtplib.SMTP_SSL(server, port)
        try:
            self.server.login(self.sender, password)
        except Exception as e:
            print(e)

    def send_email(self, subject, message):
        """Send an email

        Keyword arguments:
        subject -- str: Email subject
        message -- str: Email content/message
        """
#         email = f'Name: {self.name}\nEmail: {self.email}\nSubject: {self.subject}\nMessage: {message}'
        msg = EmailMessage()
        msg.set_content(message)
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
