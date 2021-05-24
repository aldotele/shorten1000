import uuid
from shorten1000.models import Url


def shorten(url):
    uid = str(uuid.uuid4())[:5]
    new_url = Url(link=url, uuid=uid)
    new_url.full_clean()
    new_url.save()
    return uid