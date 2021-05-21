from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.core.exceptions import ValidationError, ObjectDoesNotExist


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
    if request.method == 'GET':
        try:
            url_details = Url.objects.get(uuid=pk)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('enter a valid shortened url.')
        return redirect(url_details.link)
    else:
        return HttpResponseNotAllowed()