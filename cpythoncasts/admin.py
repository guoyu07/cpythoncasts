#coding:utf-8

from django.contrib import admin
from django.forms import ModelChoiceField
 
from cpythoncasts.models import Userinfo,Video
from exam.models import Question,Category,Answer


class UserinfoChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.user.username

class UserinfoAdmin(admin.ModelAdmin):
	list_display=('user_username',)
	def user_username(self,instance):
		return instance.user.username

class VideoAdmin(admin.ModelAdmin):
	list_display=('title',)
	

class CategoryAdmin(admin.ModelAdmin):
	list_display=('name',)

admin.site.register(Userinfo,UserinfoAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Category,CategoryAdmin)
