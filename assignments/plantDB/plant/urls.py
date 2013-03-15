from django.conf.urls import patterns, url

from plant import views

# can also import the functions and call them as objects...
# see here: https://docs.djangoproject.com/en/1.5/topics/http/urls/
urlpatterns = patterns('plant.views',
    (r'^$', 'index'),
    (r'^(?P<plant_id>\d+)/$', 'plantDetail'),
    (r'^bloom_time/(?P<pk>[a-zA-Z]+)/$', 'subIndex'),
    (r'^plant_type/(?P<pk>[a-zA-Z]+)/$', 'subIndex'),
# converting spaces to underscores?
    (r'^sun_needs/(?P<pk>[\w-]+)/$', 'subIndex'),
    #file upload for images
    #graphic representation thingy?
)