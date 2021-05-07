from django.conf import settings
import requests


def parse_authorization_header(header):
    splitted = header.decode().split(' ')
    if len(splitted) == 0:
        return None
    if len(splitted) == 1:
        return splitted[0]
    return splitted[1]


def get_internal_headers():
    return {
        'Authorization': settings.SECRET_KEY
    }


def validate_user_auth(token):
    url = settings.INTERNAL_AUTH_ADDR + 'i/validate/'
    data = {'token': token}
    resp = requests.post(url, data=data, headers=get_internal_headers())
    try:
        return resp.json()['user_id']
    except:
        return -1
