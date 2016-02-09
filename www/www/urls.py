#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls import url, include
from django.contrib import admin

from home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', admin.site.urls),
]
