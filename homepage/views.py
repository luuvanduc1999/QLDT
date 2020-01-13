from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import ScheduleWeek,Notification,Event, Document
from django.core.paginator import Paginator

def sheduleweek(request):
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
    return render(request, 'scheduleweek.html', {'items':items})

def aboutme(request):
    return render(request, 'about-me.html')
    
def home(request):
    scheduleWs=ScheduleWeek.objects.all().order_by('-id')
    notis=Notification.objects.all().order_by('-id')
    events=Event.objects.all().order_by('-id')
    docs=Document.objects.all().order_by('-id')
    return render(request, 'home.html', {'scheduleWs':scheduleWs, 'notis':notis, 'events':events, 'docs':docs})
