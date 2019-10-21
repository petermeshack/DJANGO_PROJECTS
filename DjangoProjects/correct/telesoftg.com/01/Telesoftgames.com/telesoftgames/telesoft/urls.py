from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^telesofthardwares/$', views.hardware, name='telesofthardwares'),
    url(r'^telesoftsoftwares/$', views.software, name='telesoftsoftwares'),
    url(r'^blog/$', views.blog, name='blog'),
]