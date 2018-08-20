# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'demo.views',
    (r'^$', 'index'),
    (r'^app_list/$', 'app_list'),
)
