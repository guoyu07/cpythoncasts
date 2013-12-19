#coding:utf-8
from qa.models import Questions,Answers

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView

from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def QRead(request,pk):
	 q     = Questions.objects.get(id=pk)
	 allas = Answers.objects.filter(questionid=pk) 
         return render_to_response('qa/questions_read.html',{'q':q,'allas':allas,'user':request.user},context_instance=RequestContext(request))

def QRecommend(request,qid,aid):
	q    = Questions.objects.get(id=qid)
	if q.author.username == request.user.username:
		q.recommend = aid
		q.save()
        return HttpResponseRedirect(reverse('questions-read',args=(qid,) ))


class ACreateView(CreateView):
	model  = Answers
	fields = ['content']
        def form_valid(self,form):
               form.instance.author     = self.request.user
	       form.instance.questionid = self.kwargs.get('pk')

	       questionid               = self.kwargs.get('pk')
	       q = Questions.objects.get(id=questionid)
	       q.counts += 1
	       q.save()

               super(ACreateView, self).form_valid(form)
               return HttpResponseRedirect(reverse('questions-read',args=(questionid,)) )



class QCreateView(CreateView):
	model  = Questions
	fields = ['title','content','bingo','min_people']
        def form_valid(self,form):
               form.instance.author = self.request.user
               return super(QCreateView, self).form_valid(form)


class QListView(ListView):
	model=Questions
	def get_context_data(self, **kwargs):
                  context    = super(QListView, self).get_context_data(**kwargs)
                  context.update({'user':self.request.user})
                  return context


class QUpdateView(UpdateView):
	model=Questions
	fields = ['title','content','bingo','min_people']
        def form_valid(self,form):
               form.instance.author = self.request.user
               return super(QUpdateView, self).form_valid(form)
	def get_object(self):
                objects    = self.model.objects.get(id=self.kwargs.get('pk'),\
                             author=self.request.user)
		return objects
	

class QDeleteView(DeleteView):
	model=Questions
    	success_url = reverse_lazy('questions-list')
	def get_object(self):
                 objects    = self.model.objects.get(id=self.kwargs.get('pk'),\
                              author=self.request.user)
                 return objects




########################################
'''
from django.conf.urls.defaults import patterns, url

class register_model:
	def __init__(self,model):
		self.model = model
		self.name   = model._meta.object_name.lower()
		self.create(model)
	def create(self,model):
		cview  = CreateView.as_view(model=model)
		urls   = url(r"%s/add"%self.name,cview,name="%s-add"%self.name)
		urlpatterns += patterns('',urls,)

	def list(self,model):
		clist  = ListView.as_view(model=model)
		urls   = url(r"%s/list"%self.name,clist,name="%s-list"%self.name)
		urlpatterns += patterns('',urls,)

	def update(self,model):	
		cupdate  = UpdateView.as_view(model=model)
		urls   = url(r"%s/edit/(?P<pk>\d+)"%self.name,cupdate,name="%s-edit"%self.name)
		urlpatterns += patterns('',urls,)
	def delete(self,model):
		cdelete  = DeleteView.as_view(model=model,success_url = reverse_lazy('%s-list'%self.name))
		
		urls   = url(r"%s/delete/(?P<pk>\d+)"%self.name,cdelete,name="%s-edit"%self.name)
		urlpatterns += patterns('',urls,)
'''
