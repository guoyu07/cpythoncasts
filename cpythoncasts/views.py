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
