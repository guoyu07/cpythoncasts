from django.conf.urls import patterns, include, url


from qa.views import *
from qa.models import Questions

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', QListView.as_view(queryset=Questions.objects.order_by('-id'))),
    url(r'^questions/add$', QCreateView.as_view(), name='questions-add'),
    url(r'^questions/list$', QListView.as_view(queryset=Questions.objects.order_by('-id')), name='questions-list'),
    url(r'^questions/delete/(?P<pk>\d+)/$', QDeleteView.as_view(), name='questions-del'),
    url(r'^questions/update/(?P<pk>\d+)/$', QUpdateView.as_view(), name='questions-update'),
    url(r'^questions/view/(?P<pk>\d+)$', QRead, name='questions-read'),

    url(r'^questions/recommend/(\d+)/(\d+)',QRecommend,name='questions-recommend'),

    url(r'^answers/add/(?P<pk>\d+)/$', ACreateView.as_view(), name='answers-add'),
#    url(r'^register/$', 'qa.views.register'),
#    url(r'^login$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
#    url(r'^logout$', 'django.contrib.auth.views.logout'),
)
