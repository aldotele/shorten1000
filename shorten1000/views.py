from django.shortcuts import render, redirect
from .models import Url
# added below
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy, reverse


class UrlCreateView(CreateView):
    model = Url
    fields = ['link']
    template_name = 'base.html'
    #success_url = reverse_lazy('show')

    def get_success_url(self):
        return reverse('show_short_url', args=[self.object.pk])


class ShowShortUrlView(DetailView):
    model = Url
    context_object_name = 'url'
    template_name = 'show.html'


class RedirectUrlView(DetailView):
    model = Url
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def render_to_response(self, context, **response_kwargs):
        return redirect(self.object.link)