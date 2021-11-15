from dotenv import load_dotenv
import os
import pytest
from dill_tils.email import Email

load_dotenv()


def test_login():
    recipient = os.environ['RECIPIENT']
    sender = os.environ['SENDER']
    password = os.environ['PASSWORD']
    server = os.environ['SERVER']
    port = int(os.environ['PORT'])
    e = Email(recipient, sender, password, server, port)
    output = e.__init__(recipient, sender, password, server, port)
    assert output == None


def test_send():
    recipient = os.environ['RECIPIENT']
    sender = os.environ['SENDER']
    password = os.environ['PASSWORD']
    server = os.environ['SERVER']
    port = int(os.environ['PORT'])
    output = Email(recipient, sender, password, server, port)
    output = output.send_email('Subject', 'Message')
    assert output == True
