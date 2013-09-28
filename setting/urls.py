#coding:utf-8
from django.conf.urls import patterns,include,url
from .views import *

urlpatterns =patterns('',
	# url(r'^$,)
	url(r'profile/$',InfoView.List.as_view(),name='profile'),
	url(r'profile/edit/$',InfoView.Update.as_view(),name='profile_edit'),
    url(r'profile/(?P<pk>\d+)/$', InfoView.Update.as_view(), name='profile_edit'),

    url(r'tabs/$', VideoView.List.as_view(), name='tabs'),
    url(r'tabs/add/$', VideoView.Create.as_view(), name='set_video_add'),
    url(r'tabs/(?P<pk>\d+)/$', VideoView.Update.as_view(), name='set_video_update'),
    url(r'tabs/(?P<pk>\d+)/delete/$', VideoView.Delete.as_view(), name='set_video_delete'),
   
    url(r'form/$', QuestionView.List.as_view(), name='formstyle1'),
    url(r'form/add/$', QuestionView.Create.as_view(), name='set_question_add'),
    url(r'from/(?P<pk>\d+)/$', QuestionView.Update.as_view(), name='set_question_update'),
    url(r'from/(?P<pk>\d+)/delete/$', QuestionView.Delete.as_view(), name='set_question_delete'),
    url(r'faq/$',faqquestion),
)
