#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import *


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'cpythoncasts.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT , 'show_indexes':True}),

    url(r'^grappelli/', include('grappelli.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),
#以下是主页页面等信息
	url(r'^$',unify),
    url(r'^videos/$', unifyallvideos),
	url(r'^lesson/$', unifylesson),
    url(r'^learn/$', unifylearn),
    url(r'^blog/$', unifyblog),
	url(r'^teachers/$', unifyteachers),
#以下是login等信息
    url(r'^login/$',unifylogin),
    url(r'^register/$',unifyregister),
    url(r'^logout/$',unifylogout),
#以下是test页面等信息
    url(r'^collection/$', unifycollection),
    url(r'^test/$',unifytest),
    url(r'^map/$',unifymap),
    url(r'^unifycontentpage/$',unifycontentpage),
    url(r'^unifypage/$',unifypage),
)
