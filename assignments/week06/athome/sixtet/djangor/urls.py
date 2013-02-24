from django.conf.urls import patterns, url, include
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from djangor.models import Entry

def stub(request, *args, **kwargs):
    return HttpResponse('stub view', mimetype="text/plain")

#urls:
#all entries in a list
#a single entry, including title, text, pub date, author
#a list of all entries by a particular author

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Entry.objects.all().order_by('-publish_date')[:5],
            context_object_name='blogness',
            template_name="djangor/blog.html"
        ),
        name="index view"),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Entry,
            template_name="djangor/entry.html"
        ),
        name="entry"), 
    url(r'^archive/$',
        ListView.as_view(
            queryset=Entry.objects.all().order_by('-publish_date'),
            context_object_name='archive',
            template_name="djangor/archive.html"
        ),
        name="archive"),       
    url(r'^authors/$',
        ListView.as_view(
            queryset=Entry.objects.all().order_by('entry_author'),
            context_object_name='authors',
            template_name="djangor/authors.html"
        ),
        name="authors"),                
)        