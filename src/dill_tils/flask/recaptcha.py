import requests
import json


def is_human(captcha_response: dict, secret: str):
    """
    Validating recaptcha response from google server
    Returns True captcha test passed for submitted form else returns False.

    Keyword arguments:
    captcha_response -- dict: contains users response to captcha challenge
    secret -- str: Secret key for Google reCAPTCHA
    """
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify",
                             payload)
    response_text = json.loads(response.text)
    return response_text['success']
