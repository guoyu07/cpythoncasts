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



from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class InfoView:
	class Update(UpdateView):
                model         = Userinfo
		#template_name = "account/set_info_list.html" 
		template_name = "setting/profile_update.html" 
		fields        = ['intro','photo']

		def get_object(self):
			return self.model.objects.get(user=self.request.user)

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

	class Detail(DetailView):
                model         = Userinfo
		template_name = "setting/profile.html" 
		fields        = ['intro','photo']
		def get_object(self):
			return self.model.objects.get(user=self.request.user)

		def get_context_data(self, **kwargs):
        		context    = super(InfoView.Detail, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context


class VideoView:
        class List(ListView):
                model         = Video
		template_name = "setting/video_list.html" 
		def get_queryset(self):
			return self.model.objects.filter(user=self.request.user)
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.List, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context

        class Create(CreateView):
                model = Video
		template_name = "setting/video_add_form.html" 
                fields=['title','intro','url','keyword','order']
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
		template_name = "setting/video_add_form.html" 
                fields        = ['title','intro','url','keyword','order']
		def get_object(self):
			objects    = Video.objects.get(id=self.kwargs.get('pk'),\
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
		def get_getobject(self):
			info       = set_common(self.request)
			objects    = Video.objects.filter(id=self.kwargs.get('pk'),\
					user=self.request.user)
        		return objects

