#coding:utf-8
import datetime
import os

from django.shortcuts import render_to_response,redirect
from django.template import Template, Context
from django.template import RequestContext

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy

from cpythoncasts.models import *
#from .forms import *

def base(request):
    return render_to_response('unify/base.html',context_instance=RequestContext(request))

def learn(request):
    return render_to_response('unify/learn.html',context_instance=RequestContext(request))

def course(request):
    return render_to_response('unify/course.html',context_instance=RequestContext(request))

def douban(request):
    return render_to_response('unify/douban.html',context_instance=RequestContext(request))

def bootstrap(request):
    return render_to_response('unify/bootstrap.html',context_instance=RequestContext(request))

def carousel(request):#轮番显示页面
    return render_to_response('unify/carousel.html',context_instance=RequestContext(request))

def done(request):
    return render_to_response('unify/done.html',context_instance=RequestContext(request))

def unifytest(request):
    return render_to_response('unify/unifytest.html',context_instance=RequestContext(request))
def cleancanvas(request):
    return render_to_response('unify/cleancanvas.html',context_instance=RequestContext(request))
def teeks(request):
    return render_to_response('unify/teeks.html',context_instance=RequestContext(request))

def unify(request):#unify页面
    return render_to_response('unify/unify.html',context_instance=RequestContext(request))
def unifyclass(request):#unify课程页面
    return render_to_response('unify/unifyclass.html',context_instance=RequestContext(request))
def unifyallvideos(request):#unify视频页面
    return render_to_response('unify/unifyallvideos.html',context_instance=RequestContext(request))
def unifycollection(request):#unifyclass
    return render_to_response('unify/unifycollection.html',context_instance=RequestContext(request))
def unifylesson(request):#unifylesson
    return render_to_response('unify/unifylesson.html',context_instance=RequestContext(request))
def unifyteachers(request):#unifyteachers
    return render_to_response('unify/unifyteachers.html',context_instance=RequestContext(request))
def unifyblog(request):#unifyblog
	return render_to_response('unify/unifyblog.html',context_instance=RequestContext(request))
