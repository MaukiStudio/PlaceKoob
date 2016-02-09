#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls import url, include
from django.contrib import admin

from accounts.views import register


urlpatterns = [
    url(r'^register/', register),
]
