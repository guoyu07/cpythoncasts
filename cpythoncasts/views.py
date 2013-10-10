#coding:utf-8
import datetime
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login,logout as user_logout
from django.contrib.auth.views import login 
from django.shortcuts import render_to_response,redirect
from django.template import Template, Context
from django.template import RequestContext
from admin import *

from .forms import UserForm
from .models import *

def get_retdata(active=None):
    	retdata={'unify':'','unifyallvideos':'','unifylesson':'','unifylearn':'','unifyblog':'','unifyteachers':''}
	if active:
		retdata[active] ='active'
	return retdata


def unify(request):#unify主页
    retdata = get_retdata('unify')
    retdata['username'] = request.user.username
    retdata['id']       = request.user.id
    return render_to_response("unify.html",retdata) 

def unifyallvideos(request):#unify视频页面
    retdata = get_retdata('unifyallvideos')
    return render_to_response('unifyallvideos.html',retdata,context_instance=RequestContext(request))

def unifylesson(request):#unifylesson页面
    retdata = get_retdata('unifylesson')
    return render_to_response('unifylesson.html',retdata,context_instance=RequestContext(request))

def unifylearn(request):#unifylearn课程页面
    retdata = get_retdata('unifylearn')
    return render_to_response('unifylearn.html',retdata,context_instance=RequestContext(request))
    
def unifyblog(request):#unifyblog页面
    retdata = get_retdata('unifyblog')
    return render_to_response('unifyblog.html',retdata,context_instance=RequestContext(request))

def unifyteachers(request):#unifyteachers页面
    retdata = get_retdata('unifyteachers')
    return render_to_response('unifyteachers.html',retdata,context_instance=RequestContext(request))

#####user account matters
def unifylogin(request):#unifylogin页面
    error={}
    if request.method == 'POST':
           new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
	   if new_user:
           	user_login(request, new_user)
           	return redirect("/")
	   error={'error':'登录错误,请重新输入'}

    return render_to_response('unifylogin.html',error,context_instance=RequestContext(request))

def unifyregister(request):#unifyregister页面
    form = UserForm()
    if request.method == 'POST':
                form = UserForm(request.POST)
                if form.is_valid():
                        new_user = form.save()
                        # auto login
                        new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
                        user_login(request, new_user)
                        info = Userinfo(user=request.user)
                        info.save()
                        return redirect("/")

    return render_to_response('unifyregister.html',{'form':form},context_instance=RequestContext(request))

def unifylogout(request):#logout页面
    user_logout(request)
    return redirect('/')

###special pages
def unifymap(request):#google map定位我们
    retdata = get_retdata('unifyteachers')
    return render_to_response('unifymap.html',retdata,context_instance=RequestContext(request))

def unifycontentpage(request):#contentpage页面
    retdata = get_retdata('unifylesson')
    return render_to_response("unifycontentpage.html",retdata,context_instance=RequestContext(request))

def unifypage(request):#page页面
    retdata = get_retdata('unifylearn')
    return render_to_response("unifypage.html",retdata,context_instance=RequestContext(request))

def unifycollection(request):#unifycollection页面
    retdata = get_retdata('unifyallvideos')
    return render_to_response('unifycollection.html',retdata,context_instance=RequestContext(request))
def unifytest(request):#test测试界面
    return render_to_response('unifytest.html',context_instance=RequestContext(request))
