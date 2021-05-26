from django import forms
from shorten1000.models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['link']