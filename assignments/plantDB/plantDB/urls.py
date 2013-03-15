from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^plants/', include('plant.urls')),
#     url(r'^plants/bloom_time/', 'plant.views.bloomsIndex', name='bloomsIndex'),

    url(r'^admin/', include(admin.site.urls)),
)
