import requests
from requests.exceptions import ConnectionError


def edit_url(url):
    if 'https://' not in url and 'http://' not in url:
        url = 'https://' + url
    return url


def is_url_existing(url):
    try:
        request = requests.get(url)
    except ConnectionError:
        #print('Web site does not exist')
        return False
    else:
        #print('Web site exists')
        return True

