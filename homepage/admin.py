from django.contrib import admin
from .models import ScheduleWeek, Notification, Event, Document
from django.contrib.auth.models import Group
from datetime import datetime   
from django.utils.html import format_html

# Register your models here.
@admin.register(ScheduleWeek)
class ScheduleW(admin.ModelAdmin):

    def has_delete_permission(self,request,object=None):
        return False
    
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="300px"/>  '.format(obj.thumb.url))
    image_tag.short_description ='Thumb'
    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['id', 'title', 'image_tag', 'submission_date', 'editb']
    ordering=['-id']
    list_display_links = ['title','editb']
    search_fields=['title', 'note']
    readonly_fields=['id']
    fields=['id','title','note', 'thumb', 'image', 'caption']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.submission_date=datetime.now()
        super().save_model(request, obj, form, change)

@admin.register(Notification)
class Notis(admin.ModelAdmin):

    def has_delete_permission(self,request,object=None):
        return False
    
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="300px"/>  '.format(obj.thumb.url))
    image_tag.short_description ='Thumb'
    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['id', 'title', 'image_tag', 'submission_date', 'editb']
    ordering=['-id']
    list_display_links = ['title','editb']
    search_fields=['title', 'note']
    readonly_fields=['id']
    fields=['id','title','note', 'thumb', 'file', 'caption']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.submission_date=datetime.now()
        super().save_model(request, obj, form, change)

@admin.register(Event)
class Events(admin.ModelAdmin):

    def has_delete_permission(self,request,object=None):
        return False
    
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="300px"/>  '.format(obj.thumb.url))
    image_tag.short_description ='Thumb'
    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['id', 'title', 'image_tag', 'submission_date', 'editb']
    ordering=['-id']
    list_display_links = ['title','editb']
    search_fields=['title', 'note']
    readonly_fields=['id']
    fields=['id','title','note', 'thumb', 'image', 'caption']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.submission_date=datetime.now()
        super().save_model(request, obj, form, change)

@admin.register(Document)
class Docs(admin.ModelAdmin):

    def has_delete_permission(self,request,object=None):
        return False
    
    def image_tag(self, obj):
        return format_html(' <img src="{}" width="300px"/>  '.format(obj.thumb.url))
    image_tag.short_description ='Thumb'
    def editb(self, obj):
        return format_html(' <img src="{}" width="30px"/>  '.format(obj.edit.url))
    editb.short_description = ''

    list_display = ['id', 'title', 'image_tag', 'submission_date', 'editb']
    ordering=['-id']
    list_display_links = ['title','editb']
    search_fields=['title', 'note']
    readonly_fields=['id']
    fields=['id','title','note', 'thumb', 'file', 'caption']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.submission_date=datetime.now()
        super().save_model(request, obj, form, change)
