from django.conf.urls import url
from django.contrib import admin
from edit_info import views

urlpatterns = [
    url(r'^profile/$', views.edit_hub, name="edit hub"),
    url(r'^profile/create/$', views.create, name="create project"),
    url(r'^project/edit/(?P<project_id>[0-9]+)$', views.edit_project, name="edit project"),
    url(r'^profile/info/(?P<counselor_id>[0-9]+)$', views.edit_counselor, name="edit counselor"),
]
