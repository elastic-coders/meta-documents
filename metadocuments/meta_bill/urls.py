from __future__ import absolute_import

from django.conf.urls import patterns

from . import application

urlpatterns = patterns(
    '',
    *application['urls']
)
