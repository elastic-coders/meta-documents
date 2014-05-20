from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import (BillListView, BillDetailView)

urlpatterns = patterns(
    'views',
    url(r'^bill$', BillListView.as_view()),
    url(r'^bill/(?P<pk>\d+)$', BillDetailView.as_view()),
)
