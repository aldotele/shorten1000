from django.urls import path
from . import views
from shorten1000.views import UrlCreateView, ShowShortUrlView, RedirectUrlView


urlpatterns = [
    #path('', views.base, name='base'),
    path('', views.index, name='base'),
    #path('create', views.create, name='create'),
    #path('<str:pk>', views.go, name='go'),
    # added
    path('form', UrlCreateView.as_view(), name='form'),
    #path('show', show, name='show'),
    path('show/<int:pk>', ShowShortUrlView.as_view(), name='show_short_url'),
    path('go/<slug:uuid>', RedirectUrlView.as_view(), name='redirect')
]
