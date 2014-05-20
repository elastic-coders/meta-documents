from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import (ReceiptListView, ReceiptDetailView)

urlpatterns = patterns(
    'views',
    url(r'^receipt$', ReceiptListView.as_view()),
    url(r'^receipt/(?P<pk>\d+)$', ReceiptDetailView.as_view()),
)
