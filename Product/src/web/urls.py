from django.conf.urls import url
from django.contrib import admin
#specify views
#from .views import ()
urlpatterns = [
    url(r'^list$', "web.views.project_list"),
]
