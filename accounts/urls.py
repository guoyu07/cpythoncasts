from django.conf.urls import patterns, include, url
from .views import InfoView,VideoView,QuestionView

urlpatterns = patterns('',
    url(r'login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout'),
    url(r'register/$', 'accounts.views.register'),
    url(r'set/$', 'accounts.views.set',name='set'),


    url(r'info_edit/(?P<pk>\d+)/$', InfoView.Update.as_view(), name='set_info_update'),

    url(r'videos/$', VideoView.List.as_view(), name='set_video_list'),
    url(r'video/add/$', VideoView.Create.as_view(), name='set_video_add'),
    url(r'video/(?P<pk>\d+)/$', VideoView.Update.as_view(), name='set_video_update'),
    url(r'video/(?P<pk>\d+)/delete/$', VideoView.Delete.as_view(), name='set_video_delete'),
   
    url(r'questions/$', QuestionView.List.as_view(), name='set_question_list'),
    url(r'question/add/$', QuestionView.Create.as_view(), name='set_question_add'),
    url(r'question/(?P<pk>\d+)/$', QuestionView.Update.as_view(), name='set_question_update'),
    url(r'question/(?P<pk>\d+)/delete/$', QuestionView.Delete.as_view(), name='set_question_delete'),


)
