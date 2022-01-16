import requests, os
from secret_keys import EMAIL_TO


def send_email(content):
    url = os.environ['TRUSTIFI_URL']+'/api/i/v1/email'

    payload = """{\"recipients\":[{\"email\":\"""" + EMAIL_TO + """\"}],\"title\":\"""" + content + """\",\"html\":\"""" + content + """\"}"""
    headers = {
        'x-trustifi-key': os.environ['TRUSTIFI_KEY'],
        'x-trustifi-secret': os.environ['TRUSTIFI_SECRET'],
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', url, headers=headers, data=payload)
    print(response.json())
    print('Email enviado com sucesso!')
