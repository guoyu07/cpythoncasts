#coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Category(models.Model):
	name      = models.CharField(max_length=128)
	parent    = models.ForeignKey('self',blank=True,null=True)

    	def get_absolute_url(self):
          return reverse('set_qcate_update', kwargs={'pk': self.pk})
	def __unicode__(self):
		return self.name

class Question(models.Model):
    title     = models.TextField()
    user      = models.ForeignKey(User)
    category  = models.ForeignKey(Category,default=0,null=True)
    answerkey = models.CharField(max_length=128)
    status    = models.CharField(max_length=64,default='close')
    types     = models.CharField(max_length=64,default='select') 

    def get_absolute_url(self):
          return reverse('set_question_update', kwargs={'pk': self.pk})

class Answer(models.Model):
	question  = models.ForeignKey(Question)
	user      = models.ForeignKey(User)
	answerkey = models.CharField(max_length=128)
	bingo     = models.IntegerField(default=2) #0:error;1:ok,2:system not check 
	
	
