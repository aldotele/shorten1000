from django.urls import path
from . import views
from shorten1000.views import UrlCreateView, ShowShortUrlView, RedirectUrlView


urlpatterns = [
    path('', views.index, name='base'),
    # added
    path('form', UrlCreateView.as_view(), name='form'),
    path('show/<int:pk>', ShowShortUrlView.as_view(), name='show_short_url'),
    path('go/<slug:uuid>', RedirectUrlView.as_view(), name='redirect')
]
