from django.conf.urls import include, url, patterns
from django.contrib import admin
from main import views as main_views
from familia import views as familia_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^familia/register/$', familia_views.register, name='register'),
    url(r'^familia/login/$', familia_views.login, name='login'),
    url(r'^main/', include('main.urls')), 
    url(r'^$', main_views.index, name='index'),
)
