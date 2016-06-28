from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^select_picture/$', views.select_picture, name='result'),
    url(r'^result/(?P<pic_id>[0-9]\d+)$', views.result, name='result'),
    url(r'^update/$', views.update, name='result'),
]