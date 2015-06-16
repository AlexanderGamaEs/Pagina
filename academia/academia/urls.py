from django.conf.urls import include, url, patterns
from django.contrib import admin
from main import views as main_views
from academiaCore import views as core_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', main_views.index, name='index'),
    url(r'^main/', include('main.urls')), 
    url(r'^user/register/$', core_views.register, name='register'),
)
