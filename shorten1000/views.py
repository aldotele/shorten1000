from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, HttpResponseNotAllowed
from django.core.exceptions import ValidationError


def index(request):
    return render(request, "index.html")


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        try:
            new_url = Url(link=url, uuid=uid)
            new_url.full_clean()
            new_url.save()
        except ValidationError:
            return HttpResponse('The Url is not valid.')
        return HttpResponse(uid)
    else:
        return HttpResponseNotAllowed('a url must be provided')


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)