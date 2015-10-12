from django.conf.urls import patterns, url
from KnightsAssistantPlanner import views

urlpatterns = patterns('',
              url(r'^$', views.index, name='index'),
              url(r'^newspage|^newsPage|^NewsPage', views.newsPage, name='newsPage'),
              url(r'^myhealth|^Myhealth|^MyHealth', views.myHealth, name='myHealth'),
              url(r'^myCalendar|^mycalendar', views.CalendarNp, name='CalendarNp'),
              url(r'^(Calendar|calendar)/(?P<Date>[\w\-]+)/$', views.Calendar, name='Calendar'),
              url(r'^Calendar|^calendar', views.CalendarNp, name='CalendarNp'),
              )