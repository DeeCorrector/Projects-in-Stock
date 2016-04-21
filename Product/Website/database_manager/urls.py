from django.conf.urls import url
from django.contrib import admin
#specify views
from database_manager import views

urlpatterns = [
    url(r'^database/$', views.update_database_view, name="update_db"),
    url(r'^database/all/$', views.update_all_counselors, name="update_db_all"),
    url(r'^database/specific/$', views.update_specific_counselor, name="update_db_specific"),
]
