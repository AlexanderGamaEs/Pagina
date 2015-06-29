from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^rest/(?P<pk>)/$', views.SectionList.as_view()),)
