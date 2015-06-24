from django.conf.urls import include, url, patterns
from django.contrib import admin
from main import views as main_views
from familia import views as familia_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^familia/', include('familia.urls')),
    url(r'^main/', include('main.urls')), 
    url(r'^$', main_views.index, name='index'),
)
