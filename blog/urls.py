"""
Date: 2019--22 09:54
User: yz
Email: 1147570523@qq.com
Desc:

"""
from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
   url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
   url(r'^category/(?P<id>\d+)/$', views.category, name='category'),
   url(r'^tags/(?P<id>\d+)/$', views.tags, name='tags'),
]