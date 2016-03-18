from django.conf.urls import url, include

from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^index/$', views.index,name = 'index'),
    url(r'^form/$', views.add_new,name = 'form'),
    url(r'^excel/$', views.generate_xls,name = 'generate_xls'),
    url(r'^login/$', views.logged_in,name = 'logged_in'),
]