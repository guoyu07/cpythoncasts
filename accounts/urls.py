from django.conf.urls import patterns, include, url
from .views import TeacherView,VideoView

urlpatterns = patterns('',
    url(r'login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout'),
    url(r'register/$', 'accounts.views.register'),
    url(r'set/$', 'accounts.views.set'),
    url(r'apply_teacher$', 'accounts.views.applyteacher'),


    url(r'teacher_edit/(?P<pk>\d+)/$', TeacherView.Update.as_view(), name='set_teacher_update'),
    url(r'videos/$', VideoView.List.as_view(), name='set_video_list'),
    url(r'video/add/$', VideoView.Create.as_view(), name='set_video_add'),
    url(r'video/(?P<pk>\d+)/$', VideoView.Update.as_view(), name='set_video_update'),
    url(r'video/(?P<pk>\d+)/delete/$', VideoView.Delete.as_view(), name='set_video_delete'),
)
