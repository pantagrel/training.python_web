import urllib
import urllib2
import json

from pprint import pprint

base = 'http://maps.googleapis.com/maps/api/geocode/json'
addr = '6708 27th Ave NW, Seattle, WA 98117'
data = {'address': addr, 'sensor': False}
query = urllib.urlencode(data)
res = urllib2.urlopen('?'.join([base, query]))
response = json.load(res)
pprint(response)


# base = 'http://api.techsavvy.io/jobs'
# search = 'python+web?limit=20'
# res = urllib2.urlopen('/'.join([base, search]))
# response = json.load(res)
# print type(response)
# print response.keys()
# print response['count']
# for post in response['data']:
# 	for key in sorted(post.keys()):
# 		print "%s:\n	%s" % (key, post[key])
# 	print


# saving memory on loading (for huge data sets, for processing chunks at a time)
page = urllib2.urlopen(url)
json.load(page)


