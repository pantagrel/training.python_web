from django.conf.urls import patterns, url

from plant import views

urlpatterns = patterns('',
    #ex: /plants/
    url(r'^$', views.index, name='index'),
    #ex: /plants/[common_name]
#     url(r'^(P<plant_name>\)[A-Za-z]/$', views.plantDetail, name='plantDetail'),
    #ex: /plants/5/
    url(r'^(?P<plant_id>\d+)/$', views.plantDetail, name='plantDetail'),
    url(r'^(?P<bloom_time>\[A-Za-z]+)/$', views.bloomsIndex, name='bloomsIndex'),
)