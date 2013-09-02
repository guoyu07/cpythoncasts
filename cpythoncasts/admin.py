#coding:utf-8

from django.contrib import admin
from django.forms import ModelChoiceField
 
from cpythoncasts.models import Teacher,Video


class TeacherChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.user.username

class TeacherAdmin(admin.ModelAdmin):
	list_display=('user_username',)
	def user_username(self,instance):
		return instance.user.username

class VideoAdmin(admin.ModelAdmin):
	list_display=('title','teacher_name')
	
	def teacher_name(self,instance):
		return instance.teacher.user.username

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
        	if db_field.name == "teacher":
			kwargs['queryset'] = Teacher.objects.all()
            		return TeacherChoiceField(**kwargs)
        	return super(VideoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Teacher,TeacherAdmin)

admin.site.register(Video,VideoAdmin)
