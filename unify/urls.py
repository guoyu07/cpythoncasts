from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
 	(r'^learn/$',learn),
    (r'^course/$',course),
    (r'^douban/$',douban),
    (r'^bootstrap/$',bootstrap),
    (r'^carousel/$',carousel),
    (r'^teeks/$',teeks),
    (r'^done/$',done),
    (r'^cleancanvas/$',cleancanvas),
    url(r'^unify/$',unify),
    url(r'^class/$', unifyclass),
    url(r'^videos/$', unifyallvideos),
    url(r'^blog/$', unifyblog),
	url(r'^collection/$', unifycollection),
	url(r'^lesson/$', unifylesson),
	url(r'^teachers/$', unifyteachers),
)
