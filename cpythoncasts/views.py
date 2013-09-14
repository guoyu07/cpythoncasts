#coding:utf-8
import datetime
import os

from django.shortcuts import render_to_response,redirect
from django.template import Template, Context
from django.template import RequestContext
from admin import *

def index(request):
	username = request.user.username
	return render_to_response("index.html",{'username':username}) 

def unify(request):#unify主页
    username = request.user.username
    return render_to_response("unify.html",{'username':username}) 
def unifyallvideos(request):#unify视频页面
    return render_to_response('unifyallvideos.html',context_instance=RequestContext(request))
def unifylesson(request):#unifylesson
    return render_to_response('unifylesson.html',context_instance=RequestContext(request))
def unifyclass(request):#unify课程页面
    return render_to_response('unifyclass.html',context_instance=RequestContext(request))
def unifycollection(request):#unifyclass
    return render_to_response('unifycollection.html',context_instance=RequestContext(request))

def unifyblog(request):#unifyblog
	return render_to_response('unifyblog.html',context_instance=RequestContext(request))
def unifycollection(request):#unifycollection
	return render_to_response('unifycollection.html',context_instance=RequestContext(request))
def unifyteachers(request):#unifyteachers
    return render_to_response('unifyteachers.html',context_instance=RequestContext(request))
def unifytest(request):#test测试界面
    return render_to_response('unifytest.html',context_instance=RequestContext(request))

def unifylogin(request):#unifylogin
    return render_to_response('unifylogin.html',context_instance=RequestContext(request))
def unifyregister(request):#unifyregister
    return render_to_response('unifyregister.html',context_instance=RequestContext(request))
def unifymap(request):#google map定位我们
    return render_to_response('unifymap.html',context_instance=RequestContext(request))
