from django.conf.urls import patterns, include, url

from django.contrib import admin
from document import urls as document_urls
from receipt import urls as receipt_urls
from bill import urls as bill_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'metadocuments.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(document_urls)),
    url(r'^', include(receipt_urls)),
    url(r'^', include(bill_urls)),
)
