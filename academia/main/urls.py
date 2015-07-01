from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
	    url(r'^rest/(?P<name>\w+)/$', views.SectionList.as_view()),
        url(r'^$', views.index, name='index'),)
