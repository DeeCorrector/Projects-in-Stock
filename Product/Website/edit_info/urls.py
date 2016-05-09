from django.conf.urls import url
from django.contrib import admin
from edit_info import views

urlpatterns = [
    url(r'^profile/$', views.edit_hub, name="edit_hub"),
    url(r'^profile/create/$', views.create, name="create_project"),
    url(r'^project/edit/(?P<project_id>[0-9]+)$', views.edit_project, name="edit_project"),
    url(r'^project/delete/(?P<project_id>[0-9]+)$', views.delete_project, name="delete_project"),
    url(r'^profile/info/(?P<counselor_id>[0-9]+)$', views.edit_counselor, name="edit_counselor"),
]
