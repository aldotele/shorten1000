from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Url
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from shorten1000.helper.check_url import edit_url, is_url_existing
from shorten1000.helper.shorten_url import shorten
# added below
from django.views.generic import FormView, CreateView, DetailView
from shorten1000.forms import UrlForm
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, "testempty.html")


class UrlCreateView(CreateView):
    model = Url
    fields = ['link']
    template_name = 'testform.html'
    #success_url = reverse_lazy('show')

    def get_success_url(self):
        return reverse('show_short_url', args=[self.object.pk])


class ShowShortUrlView(DetailView):
    model = Url
    context_object_name = 'url'
    template_name = 'testshow.html'


class RedirectUrlView(DetailView):
    model = Url
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def render_to_response(self, context, **response_kwargs):
        return redirect(self.object.link)


# class UrlFormView(FormView):
#     form_class = UrlForm
#     template_name = 'form.html'


# def show(request):
#     context = {"prova": "... prova ..."}
#     return render(request, "testshow.html", context)


def create(request):
    # create a unique error message for not valid Urls
    error_message = 'error: the Url is not valid'
    if request.method == 'POST':
        url = request.POST['link']
        # edit url by prepending https:// if not present
        url = edit_url(url)
        # check if website exists
        if is_url_existing(url):  # url will be shortened only if website exists
            try:
                uid = shorten(url)  # shortening url and returning token
            except ValidationError:
                return HttpResponse(error_message)
            return HttpResponse(uid)
        else:  # website does not exist
            return HttpResponse(error_message)
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