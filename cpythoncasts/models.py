#coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Teacher(models.Model):
    intro    = models.TextField()
    photo    = models.ImageField(upload_to='photo',blank=True)
    user     = models.ForeignKey(User)

    def get_absolute_url(self):
          return reverse('set_teacher_update', kwargs={'pk': self.pk})


class Video(models.Model):
    title    = models.CharField(max_length=256)
    intro    = models.TextField()
    teacher  = models.ForeignKey(Teacher)
    keyword  = models.CharField(max_length=64)
    order    = models.IntegerField(default=0)
    count    = models.IntegerField(default=0)
    url      = models.TextField()
    image    = models.ImageField(upload_to='video',blank=True)

	
    def get_absolute_url(self):
          return reverse('set_video_update', kwargs={'pk': self.pk})

