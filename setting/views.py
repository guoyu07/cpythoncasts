# coding:utf-8
import datetime
import os
# django import
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
# project import
from cpythoncasts.models import *
from exam.models import *

def set_common(request):
    info = {'video':'no'}
    username = request.user.username
    info['username'] = username
    info['id'] = request.user.id
    return info
def set(request):
    info = set_common(request)
    if request.user.is_authenticated():
        uinfo = Userinfo.objects.get(user=request.user.id)
        info['uinfo'] = uinfo
        return render_to_response('setting/setting.html', info, context_instance=RequestContext(request))
    return redirect('/login')

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

class InfoView:
    class List(ListView):
        model = Userinfo
        template_name = "setting/profile.html"
        field=['intro','photo']
        def get_queryset(self):
            return self.model.objects.filter(user=self.request.user.id)
        def get_context_data(self, **kwargs):
            context = super(InfoView.List, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
    class Update(UpdateView):
        model = Userinfo
        template_name = 'setting/profile.html'
        field = ['intro', 'photo']
        
        def get_queryset(self):
            return self.models.objects.filter(user=self.request.user.id)
        
        def get_context_date(self):
            context = super(InfoView.Update, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
        
        def form_valid(self, form):
            info = set_common(self.request)
            if form.instance.user != self.request.user.id:
                return self.form_invalid(form)
            return super(InfoView.Update, self).form_valid(form)
        
class VideoView:
    class List(ListView):
        model = Video
        template_name = "setting/tabs.html"
        def get_queryset(self):
            return self.model.objects.filter(user=self.request.user.id)
        def get_context_data(self, **kwargs):
            context = super(VideoView.List, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
    class Create(CreateView):
        model = Video
        template_name = 'setting/video_add.html'
        fields = ['title', 'intro', 'url', 'image', 'keyword', 'order']
        def get_context_data(self, **kwargs):
            context = super(VideoView.Create, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(VideoView.Create, self).form_valid(form)
    class Update(UpdateView):
        model = Video
        template_name = 'setting/video_update.html'
        fields = ['title', 'intro', 'url', 'image', 'keyword', 'order']
        def get_queryset(self):
            objects = Video.objects.filter(id=self.kwargs.get('pk'), user=request.user)
            return objects
        def get_context_data(self, **kwargs):
            context = super(VideoView.Update, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
        def form_valid(self, form):
            info = set_common(self.request)
            if form.instance.user != self.request.user:
                return self.form_invalid(form)
            return super(VideoView.Update, self).form_valid(form)
    class Delete(DeleteView):
        model = Video
        template_name = 'setting/video_delete.html'
        success_url = reverse_lazy('video_list')
        def get_queryset(self):
            info = set_common(self.request)
            objects = Video.objects.filter(id=self.kwargs.get('pk'), user=request.user)
            return objects


class QuestionView:
        class List(ListView):
            model = Question
            template_name = "setting/formstyle1.html" 
            fields = ['title', 'answerkey', 'status', 'types', 'category']
        def get_queryset(self):
            return self.model.objects.filter(user=self.request.user)
        def get_context_data(self, **kwargs):
            context = super(QuestionView.List, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context

        class Create(CreateView):
                model = Question
                template_name = "setting/formstyle1.html" 
                fields = ['title', 'answerkey', 'status', 'types', 'category']
        def get_context_data(self, **kwargs):
            context = super(QuestionView.Create, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
        def form_valid(self, form):
            form.instance.user = self.request.user 
            return super(QuestionView.Create, self).form_valid(form)

        class Update(UpdateView):
            model = Question
            template_name = "setting/set_question_form.html" 
            fields = ['title', 'answerkey', 'status', 'types', 'category']
        def get_queryset(self):
            objects = Question.objects.filter(id=self.kwargs.get('pk'), \
            user=self.request.user)
            return objects
        def get_context_data(self, **kwargs):
            context = super(QuestionView.Update, self).get_context_data(**kwargs)
            info = set_common(self.request)
            context.update(info)
            return context
        def form_valid(self, form):
            if form.instance.user != self.request.user:
                return self.form_invalid(form)
            return super(QuestionView.Update, self).form_valid(form)

        class Delete(DeleteView):
            model = Question
            template_name = "setting/set_confirm_delete.html" 
            success_url = reverse_lazy('FAQ')
        def get_queryset(self):
            info = set_common(self.request)
            objects = Quesiton.objects.filter(id=self.kwargs.get('pk'), \
            user=self.request.user)
            return objects          

def faqquestion(request):#faq page
     return render_to_response('setting/FAQ.html',context_instance=RequestContext(request))