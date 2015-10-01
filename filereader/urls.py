from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loggingin, name='loggingin'),
    #url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^getchildren/$', views.getchildren, name='getchildren'),
]
