def edit_url(url):
    if 'https://' not in url and 'http://' not in url:
        url = 'https://' + url
    return url
