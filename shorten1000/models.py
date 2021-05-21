from django.db import models


class Url(models.Model):
    link = models.URLField(max_length=2048)
    uuid = models.CharField(max_length=10)
