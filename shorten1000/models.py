from django.db import models
import secrets
from django.urls import reverse


def get_uuid():
    return secrets.token_urlsafe(5)


class Url(models.Model):
    link = models.URLField(max_length=2048)
    uuid = models.CharField(unique=True, default=get_uuid, max_length=10)

    def get_short_url(self):
        return self.uuid
        #return reverse('redirect', kwargs={'uuid', self.uuid})
