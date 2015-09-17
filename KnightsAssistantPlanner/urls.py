from django.conf.urls import patterns, url
from KnightsAssistantPlanner import views

urlpatterns = patterns('',
              url(r'^$', views.index, name='index'),
              url(r'^newspage|^newsPage|^NewsPage', views.newsPage, name='newsPage'),
              url(r'^myhealth|^Myhealth|^MyHealth', views.myHealth, name='myHealth'),
              )