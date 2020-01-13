from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from .models import ScheduleWeek,Notification,Event, Document
from django.core.paginator import Paginator

def scheduleweek(request):
    itemsX=ScheduleWeek.objects.all().order_by('-id')
    paginator = Paginator(itemsX,4)
    
    page=request.GET.get('page','1')
    items=paginator.get_page(page)
    
    try:
        items = paginator.page(page)
    except paginator.Paginator.PageNotAnInteger:
        items = paginator.page(1)
    except paginator.Paginator.EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'catalogue.html', {'items':items, 'index':1, 'ctl':'schedule-week'})

def scheduleweekItem(request, num):
    try:
        item = ScheduleWeek.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'item.html', {'item': item, 'index':1})

def notis(request):
    itemsX=Notification.objects.all().order_by('-id')
    paginator = Paginator(itemsX,4)
    
    page=request.GET.get('page','1')
    items=paginator.get_page(page)
    
    try:
        items = paginator.page(page)
    except paginator.Paginator.PageNotAnInteger:
        items = paginator.page(1)
    except paginator.Paginator.EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'catalogue.html', {'items':items, 'index':2, 'ctl':'notification'})    

def notisItem(request, num):
    try:
        item = Notification.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'item.html', {'item': item, 'index':2})


def event(request):
    itemsX=Event.objects.all().order_by('-id')
    paginator = Paginator(itemsX,4)
    
    page=request.GET.get('page','1')
    items=paginator.get_page(page)
    
    try:
        items = paginator.page(page)
    except paginator.Paginator.PageNotAnInteger:
        items = paginator.page(1)
    except paginator.Paginator.EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'catalogue.html', {'items':items, 'index':3, 'ctl':'news-event'})    

def eventItem(request, num):
    try:
        item = Event.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'item.html', {'item': item, 'index':3})

def document(request):
    itemsX=Document.objects.all().order_by('-id')
    paginator = Paginator(itemsX,4)
    
    page=request.GET.get('page','1')
    items=paginator.get_page(page)
    
    try:
        items = paginator.page(page)
    except paginator.Paginator.PageNotAnInteger:
        items = paginator.page(1)
    except paginator.Paginator.EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'catalogue.html', {'items':items, 'index':4, 'ctl':'document'})  
  
def documentItem(request, num):
    try:
        item = Document.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'item.html', {'item': item, 'index':4})  

def aboutme(request):
    return render(request, 'about-me.html')
    
def home(request):
    scheduleWs=ScheduleWeek.objects.all().order_by('-id')
    notis=Notification.objects.all().order_by('-id')
    events=Event.objects.all().order_by('-id')
    docs=Document.objects.all().order_by('-id')
    return render(request, 'home.html', {'scheduleWs':scheduleWs, 'notis':notis, 'events':events, 'docs':docs})

