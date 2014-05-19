from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import (DocumentListView, DocumentDetailView)

urlpatterns = patterns(
    'views',
    url(r'^document$', DocumentListView.as_view()),
    url(r'^document/(?P<pk>\d+)$', DocumentDetailView.as_view()),
)
