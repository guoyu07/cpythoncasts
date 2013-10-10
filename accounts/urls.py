from django.conf.urls import patterns, include, url
from .views import InfoView,VideoView


from django.contrib.auth.decorators import login_required


def url_login(regex,views, *args, **kwargs):
	return url(regex,login_required(views.as_view(),login_url='login'),*args,**kwargs)

urlpatterns = patterns('',


    url_login(r'profile/(?P<pk>\d+)/$', InfoView.Detail, name='set_profile_detail'),
    url_login(r'profile/(?P<pk>\d+)/update$', InfoView.Update, name='set_profile_update'),

    url_login(r'videos/$', VideoView.List, name='set_video_list'),
    url_login(r'video/add/$', VideoView.Create, name='set_video_add'),
    url_login(r'video/(?P<pk>\d+)/$', VideoView.Update, name='set_video_update'),
    url_login(r'video/(?P<pk>\d+)/delete/$', VideoView.Delete, name='set_video_delete'),
   
#     url(r'questions/$', QuestionView.List.as_view(), name='set_question_list'),
#     url(r'question/add/$', QuestionView.Create.as_view(), name='set_question_add'),
#     url(r'question/(?P<pk>\d+)/$', QuestionView.Update.as_view(), name='set_question_update'),
#     url(r'question/(?P<pk>\d+)/delete/$', QuestionView.Delete.as_view(), name='set_question_delete'),
)
