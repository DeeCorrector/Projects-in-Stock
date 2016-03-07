from django.conf.urls import url
from django.contrib import admin
#specify views
from web import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^projects$', views.project_list, name="project_list"),
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.project_detail, name='project_detail'),
]
