from django.conf.urls import patterns, url
from familia import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='familia'),
        url(r'^register/$', views.user_register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
)
