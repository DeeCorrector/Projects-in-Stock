from django.conf.urls import url
from django.contrib import admin
from edit_info import views

urlpatterns = [
    url(r'^counselors/(?P<counselor_id>[0-9]+)/$', views.edit_hub, name="edit hub"),

]
