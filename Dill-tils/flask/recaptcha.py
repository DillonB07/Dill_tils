import os
import requests
import json


def is_human(captcha_response: dict, secret: str = os.environ['CAPTCHA_SECRET_KEY']):
    """
    Validating recaptcha response from google server
    Returns True captcha test passed for submitted form else returns False.
    """
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify",
                             payload)
    response_text = json.loads(response.text)
    return response_text['success']
