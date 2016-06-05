from django.conf.urls import url
from django.contrib import admin
from database_manager import views

urlpatterns = [
    url(r'^database/$', views.update_database_view, name="update_db"),
    url(r'^database/all/$', views.update_all_counselors, name="update_db_all"),
    url(r'^database/specific/$', views.update_specific_counselor, name="update_db_specific"),
    url(r'^database/findnewcounselors',views.find_new_counselors, name="find_new_counselors"),
    url(r'^database/post', views.update_database_post, name="update_db_post" )
]
