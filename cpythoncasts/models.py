#coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Userinfo(models.Model):
    intro    = models.TextField()
    photo    = models.ImageField(upload_to='photo',blank=True)
    user     = models.ForeignKey(User)
    role     = models.CharField(max_length=64)

    def get_absolute_url(self):
          return reverse('set_info_update', kwargs={'pk': self.pk})


class Video(models.Model):
    title    = models.CharField(max_length=256)
    intro    = models.TextField()
    user     = models.ForeignKey(User)
    keyword  = models.CharField(max_length=64)
    order    = models.IntegerField(default=0)
    count    = models.IntegerField(default=0)
    url      = models.TextField()
    image    = models.ImageField(upload_to='video',blank=True)
    createdt = models.DateTimeField(auto_now_add=True, verbose_name=u'发布日期')

	
    def get_absolute_url(self):
          return reverse('set_video_update', kwargs={'pk': self.pk})

