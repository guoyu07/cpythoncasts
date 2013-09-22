#coding:utf-8
import datetime
import os

from django.shortcuts import render_to_response,redirect
from django.template import Template, Context
from django.template import RequestContext

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy

from cpythoncasts.models import *
from exam.models import *



def set_common(request):
	info     = {'video':'no'}
	username         = request.user.username 
	info['username'] = username
	info['id']       = request.user.id

	return info

def set(request):
	info          = set_common(request)
	if request.user.is_authenticated():
		uinfo	      = Userinfo.objects.get(user=request.user)
		info['uinfo'] = uinfo
		return render_to_response('account/set.html',info,context_instance=RequestContext(request))
	return   redirect('/login/') 


from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView


class InfoView:
	class Update(UpdateView):
                model         = Userinfo
		template_name = "account/set_info_list.html" 
		fields        = ['intro','photo']

		def get_queryset(self):
			return self.model.objects.filter(user=self.request.user)
			 
		def get_context_data(self, **kwargs):
        		context    = super(InfoView.Update, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context

		def form_valid(self,form):
			info       = set_common(self.request)
			if form.instance.user!= self.request.user:
				return self.form_invalid(form)
			return super(InfoView.Update, self).form_valid(form)


class VideoView:
        class List(ListView):
                model         = Video
		template_name = "account/set_video_list.html" 
		def get_queryset(self):
			return self.model.objects.filter(user=self.request.user)
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.List, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context

        class Create(CreateView):
                model = Video
		template_name = "account/set_video_form.html" 
                fields=['title','intro','url','image','keyword','order']
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.Create, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context
		def form_valid(self,form):
			form.instance.user = self.request.user
			return super(VideoView.Create, self).form_valid(form)

        class Update(UpdateView):
                model         = Video
		template_name = "account/set_video_form.html" 
                fields        = ['title','intro','url','image','keyword','order']
		def get_queryset(self):
			objects    = Video.objects.filter(id=self.kwargs.get('pk'),\
					user=self.request.user)
        		return objects
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.Update, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context
		def form_valid(self,form):
			info       = set_common(self.request)
			if form.instance.user != self.request.user:
				return self.form_invalid(form)
			return super(VideoView.Update, self).form_valid(form)

        class Delete(DeleteView):
                model         = Video
		template_name = "account/set_confirm_delete.html" 
                success_url   = reverse_lazy('set_video_list')
		def get_queryset(self):
			info       = set_common(self.request)
			objects    = Video.objects.filter(id=self.kwargs.get('pk'),\
					user=self.request.user)
        		return objects
class QuestionView:
        class List(ListView):
                model         = Question
		template_name = "account/set_question_list.html" 
		def get_queryset(self):
			return self.model.objects.filter(user=self.request.user)
		def get_context_data(self, **kwargs):
        		context    = super(QuestionView.List, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context

        class Create(CreateView):
                model = Question
		template_name = "account/set_question_form.html" 
                fields=['title','answerkey','status','types','category']
		def get_context_data(self, **kwargs):
        		context    = super(QuestionView.Create, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context
		def form_valid(self,form):
			form.instance.user = self.request.user 
			return super(QuestionView.Create, self).form_valid(form)

        class Update(UpdateView):
                model         = Question
		template_name = "account/set_question_form.html" 
                fields=['title','answerkey','status','types','category']
		def get_queryset(self):
			objects    = Question.objects.filter(id=self.kwargs.get('pk'),\
					user=self.request.user)
        		return objects
		def get_context_data(self, **kwargs):
        		context    = super(QuestionView.Update, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context
		def form_valid(self,form):
			if form.instance.user != self.request.user:
				return self.form_invalid(form)
			return super(QuestionView.Update, self).form_valid(form)

        class Delete(DeleteView):
                model         = Question
		template_name = "account/set_confirm_delete.html" 
                success_url   = reverse_lazy('set_question_list')
		def get_queryset(self):
			info       = set_common(self.request)
			objects    = Quesiton.objects.filter(id=self.kwargs.get('pk'),\
					user=self.request.user)
        		return objects


