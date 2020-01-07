from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .models import Student
from datetime import datetime   
from django.utils.html import format_html
import re


# Register your models here.
@admin.register(Student)
class StudentM(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="150px"/>  '.format(obj.image.url))
    image_tag.short_description = 'Ảnh thẻ'

    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['identityS', 'name', 'image_tag', 'status','editb']
    list_display_links = ['editb']
    ordering=['identityS']
    readonly_fields=['identityS']
    fields=['Years','name','gender','dob','image','status']
    

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        if (obj.identityS==''):
            x=Student.objects.all()
            count = 0
            for i in x:
                if (i.Years==obj.Years):  
                    tmp=int(re.findall('\d+', i.identityS)[0])
                    count=max(count,tmp)
            if (count==0): obj.identityS=str(obj.Years)+'001'
            else: obj.identityS=str(count+1)
        super().save_model(request, obj, form, change)

