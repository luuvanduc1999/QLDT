"""QLDT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from management import views
from homepage import views as viewsH


urlpatterns = [
    url(r'^$', viewsH.home, name='home'),
    url(r'^dashboard/', admin.site.urls),
    url(r'^about-me/',viewsH.aboutme, name='aboutme'),
    path('schedule-week/',viewsH.scheduleweek, name='scheduleweek'),
    re_path(r'^schedule-week/(\d+)/',viewsH.scheduleweekItem, name='si'),
    path('notification/',viewsH.notis, name='Notification'),
    re_path(r'^notification/(\d+)/',viewsH.notisItem, name='NotificationI'),
    path('news-event/',viewsH.event, name='newsEvent'),
    re_path(r'^news-event/(\d+)/',viewsH.eventItem, name='newsEventI'),
    path('document/',viewsH.document, name='document'),
    re_path(r'^document/(\d+)/',viewsH.documentItem, name='documentI')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)