from django.conf.urls import url
from django.contrib import admin
from edit_info import views

urlpatterns = [
<<<<<<< HEAD
    url(r'(?P<counselor_id>[0-9]+)/$', views.edit_hub, name="edit hub"),
    url(r'(?P<counselor_id>[0-9]+)/create$', views.create, name="create project"),
=======
    url(r'^profile/$', views.edit_hub, name="edit hub"),

>>>>>>> f3f7b766491bcc0b0ebb510dca183acc1cd2173e
]
