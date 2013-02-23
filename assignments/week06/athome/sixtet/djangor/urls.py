from django.conf.urls import patterns, url
from django.http import HttpResponse

from djangor.models import Entry, Archive, Author


def stub(request, *args, **kwargs):
    return HttpResponse('stub view', mimetype="text/plain")

#urls:
#all entries in a list
#a single entry, including title, text, pub date, author
#a list of all entries by a particular author

urlpatterns = patterns('',
    url(r'^$', stub, name="entry_list"),
    url(r'^(?P<pk>\d+)/$', stub, name="author_list"),
    url(r'^(?P<pk>\d+)/entry/$', stub, name="entry_detail"),
)