from django.conf.urls import patterns, url
from KnightsAssistantPlanner import views

urlpatterns = patterns('',
              url(r'^$', views.user_login, name='defalut login'),
              url(r'^newspage|^newsPage|^NewsPage', views.newsPage, name='newsPage'),
              #url(r'^myhealth|^Myhealth|^MyHealth', views.myHealth, name='myHealth'),
              url(r'^myCalendar|^mycalendar', views.CalendarNp, name='CalendarNp'),
              url(r'^(Calendar|calendar)/(?P<Date>[\w\-]+)/$', views.Calendar, name='Calendar'),
              url(r'^dayView/(?P<Date>[\w\-]+)/$', views.Daily, name='Daily'),
              url(r'^event/(?P<event_id>[\w\-]+)/$', views.event_view, name='event'),
              #craig
              url(r'^myhealth|^Myhealth|^MyHealth', views.myHealthNp, name='HealthNp'),
              #url(r'^(health|^Health)/(?P<workout_selection>[\w\-]+)/$', views.Health, name='Health'),
              url(r'^register', views.register, name='register'),
              url(r'^login', views.user_login, name='login'),
              url(r'^logout', views.user_logout, name='logout'),
              url(r'^workout/(?P<Date>[\w\-]+)/$', views.Workout, name='workout'),
              # url(r'^Calendar|^calendar', views.CalendarNp, name='CalendarNp'),
              )