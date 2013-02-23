# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.contrib import messages
from djangor.models import Entry, Archive, Author

#make something viewable...