#coding:utf-8
import datetime
import os
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login,logout as user_logout
from django.shortcuts import render_to_response,redirect
from django.template import Template, Context
from django.template import RequestContext
from admin import *



def index(request):
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    username = request.user.username
    return render_to_response("index.html",{'username':username}) 

def unify(request):#unify主页
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    retdata['username'] = request.user.username
    retdata['unify'] ='active'
    return render_to_response("unify.html",retdata) 

def unifyallvideos(request):#unify视频页面
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    retdata['unifyallvideos'] = 'active'
    return render_to_response('unifyallvideos.html',retdata,context_instance=RequestContext(request))

def unifylesson(request):#unifylesson页面
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    retdata['unifylesson'] = 'active'
    return render_to_response('unifylesson.html',retdata,context_instance=RequestContext(request))

def unifylearn(request):#unifylearn课程页面
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    retdata['unifylearn'] = 'active'
    return render_to_response('unifylearn.html',retdata,context_instance=RequestContext(request))
    
def unifyblog(request):#unifyblog页面
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    retdata['unifyblog'] = 'active'
    return render_to_response('unifyblog.html',retdata,context_instance=RequestContext(request))

def unifyteachers(request):#unifyteachers页面
    retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
    retdata['unifyteachers'] = 'active'
    return render_to_response('unifyteachers.html',retdata,context_instance=RequestContext(request))

def unifycollection(request):#unifycollection页面

    retdata={'unify':'no','unifyallvideos':'no','unifylesson':'no'}
    retdata['unifyallvideos'] = 'active'
    return render_to_response('unifycollection.html',context_instance=RequestContext(request))
def unifycollection(request):#unifycollection页面
	return render_to_response('unifycollection.html',context_instance=RequestContext(request))
def unifytest(request):#test测试界面
    return render_to_response('unifytest.html',context_instance=RequestContext(request))

def unifylogin(request):#unifylogin页面
    return render_to_response('unifylogin.html',context_instance=RequestContext(request))
def unifyregister(request):#unifyregister页面
    return render_to_response('unifyregister.html',context_instance=RequestContext(request))
def unifylogout(request):#logout页面
    user_logout(request)
    return render_to_response('/')

def unifymap(request):#google map定位我们
    return render_to_response('unifymap.html',context_instance=RequestContext(request))
def unifycontentpage(request):#contentpage页面
    return render_to_response("unifycontentpage.html",context_instance=RequestContext(request))
def unifypage(request):#page页面
    return render_to_response("unifypage.html",context_instance=RequestContext(request))