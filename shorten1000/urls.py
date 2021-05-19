from django.urls import path
from . import views

urlpatterns = [
    #path('', views.base, name='base'),
    path('', views.index, name='test'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]