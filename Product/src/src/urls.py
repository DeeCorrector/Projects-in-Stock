"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

#import the edit_info views
from edit_info import views as edit_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('web.urls')),
    url(r'^edit/', include('edit_info.urls')),

    #login urls
    url(r'^accounts/login/$', edit_views.login, name='login'),
    url(r'^accounts/auth_login/$', edit_views.auth_login),
    url(r'^accounts/logout/$', edit_views.logout, name='logout'),
]
