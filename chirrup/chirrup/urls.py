"""chirrup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from users import views as users_views
from webview import views as web_views
from chirp import views as chirp_views

urlpatterns = [
    url(r'^$', web_views.index),

    url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^register/$', users_views.RegisterUser.as_view()),

    url(r'^chirp/add$', chirp_views.get_chirp),

    url(r'^users/$', users_views.users),
    url(r'^users/(?P<username>\w+)/$', users_views.user_page),
]
