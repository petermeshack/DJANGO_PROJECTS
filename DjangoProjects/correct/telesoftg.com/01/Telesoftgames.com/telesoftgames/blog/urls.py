from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blog/blog.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Post,
        template_name="blog/post.html")),

]
# urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^gallary/$', views.gallary, name='gallary'),
#    url(r'^aboutus/$', views.aboutus, name='aboutus'),
#    url(r'^contact/$', views.contact, name='contact'),
# ]
