#coding:utf-8
import datetime
import os

from django.shortcuts import render_to_response,redirect
from django.template import Template, Context
from django.template import RequestContext

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy

from cpythoncasts.models import *
from .forms import UserForm

def register(request):
        form = UserForm()
        if request.method == 'GET':
                return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
        if request.method == 'POST':
                form = UserForm(request.POST)
                if form.is_valid():
                        new_user = form.save()
			# auto login
			new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            		login(request, new_user)
                	return redirect("/")
                else:
			return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))



def set_common(request):
	info     = {'teacher':'no','video':'no'}
	username         = request.user.username 
	info['username'] = username
	info['id']       = request.user.id

	try :
                t                = Teacher.objects.get(user=request.user)
		info ['teacher'] = t	
	except:
		pass

	return info

def set(request):

	info = set_common(request)
	
	return render_to_response('set.html',info,context_instance=RequestContext(request))


def applyteacher(request):
	if request.user.username:
		t = Teacher(user=request.user)
		t.save()

        return redirect("/accounts/set/")


from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView


class TeacherView:
	class Update(UpdateView):
                model         = Teacher
		template_name = "teacher_list.html" 
		fields        = ['intro','photo']

		def get_context_data(self, **kwargs):
        		context    = super(TeacherView.Update, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			pk         = self.kwargs.get('pk', None)	
			if int(pk) != info['teacher'].id:
				context['form'] = 'no'
			context.update(info)
        		return context


class VideoView:
        class List(ListView):
                model = Video
		template_name = "set_video_list.html" 
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.List, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context

        class Create(CreateView):
                model = Video
		template_name = "set_video_form.html" 
                fields=['title','intro','url','image','keyword','order']
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.Create, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context
		def form_valid(self,form):
			info       = set_common(self.request)
			form.instance.teacher = info['teacher']
			return super(VideoView.Create, self).form_valid(form)

        class Update(UpdateView):
                model = Video
		template_name = "set_video_form.html" 
                fields=['title','intro','url','image','keyword','order']
		def get_context_data(self, **kwargs):
        		context    = super(VideoView.Update, self).get_context_data(**kwargs)
			info       = set_common(self.request)
			context.update(info)
        		return context

        class Delete(DeleteView):
                model = Video
		template_name = "set_confirm_delete.html" 
                success_url = reverse_lazy('set_video_list')

