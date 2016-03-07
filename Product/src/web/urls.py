from django.conf.urls import url
from django.contrib import admin
#specify views
from web import views
urlpatterns = [
    url(r'^projects$', views.project_list),
]
