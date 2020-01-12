from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .models import Student,Teacher,Class
from datetime import datetime   
from django.utils.html import format_html
import re


# Register your models here.
@admin.register(Student)
class StudentM(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="150px"/>  '.format(obj.image.url))
    image_tag.short_description = 'Ảnh'

    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['identityS', 'name', 'image_tag', 'status','editb']
    list_display_links = ['editb']
    ordering=['identityS']
    readonly_fields=['identityS']
    fieldsets=(
        (None, {
            'fields' : ('Years','datebegin','image','status')
            }
        ),
        ('Thông tin cá nhân', {
            'fields' : ('name','dob','gender','hometown','ethnic','religion','addr','phonenum')
            }
        ),
        ('Gia đình', {
            'fields' : ('namedad','dobdad','jobdad','phonenumdad','namemom','dobmom','jobmom','phonenummom')
            }
        ),
    )
        
    search_fields=['identityS', 'name']

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


# Register your models here.
@admin.register(Teacher)
class TeacherM(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="150px"/>  '.format(obj.image.url))
    image_tag.short_description = 'Ảnh'

    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['identityT', 'name', 'image_tag', 'status','editb']
    list_display_links = ['name','editb']
    ordering=['identityT']
    readonly_fields=['identityT']
    fieldsets=(
        (None, {
            'fields' : ('datebegin','level','image','status')
            }
        ),
        ('Thông tin cá nhân', {
            'fields' : ('name','dob','gender','hometown','ethnic','religion','addr','phonenum')
            }
        )
    )
        
    search_fields=['identityT', 'name']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        if (obj.identityT==''):
            x=Teacher.objects.all()
            count = 0
            for i in x: 
                tmp=int(re.findall('\d+', i.identityT)[0])
                count=max(count,tmp)
            x="000"
            if (count==0): obj.identityT='GV001'
            else: obj.identityT='GV'+x[0:3-len(str(count+1))]+str(count+1)
        super().save_model(request, obj, form, change)

# Register your models here.
@admin.register(Class)
class ClassM(admin.ModelAdmin):
    def getGVCN(self, obj):
        return obj.gvcn.name
    getGVCN.short_description='Tên GVCN'

    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''


    list_display = ['identityC', 'gvcn', 'classname','editb' ]
    list_display_links = ['identityC','editb']
    ordering=['identityC']
    search_fields=['identityC', 'name']
    fields=['identityC', 'gvcn', 'classname']