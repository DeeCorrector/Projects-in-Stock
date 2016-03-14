from django.conf.urls import url
from django.contrib import admin
from edit_info import views

urlpatterns = [
    url(r'^profile/$', views.edit_hub, name="edit hub"),

]
