#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Questions(models.Model):
    title      = models.CharField(verbose_name='标题',max_length=256)
    content    = models.TextField(verbose_name='内容')
    bingo      = models.CharField(verbose_name='答案',max_length=256,blank=True)
    min_people = models.IntegerField(verbose_name='至少回答人数(用于揭晓答案)',default=5)
    author     = models.ForeignKey(User)
    counts     = models.IntegerField(default=0,blank=True)
    recommend  = models.IntegerField(blank=True,null=True)
    cd         = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('questions-list')


class Answers(models.Model):
    questionid = models.IntegerField()
    content    = models.TextField()
    author     = models.ForeignKey(User)
    cd         = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('questions-list')

