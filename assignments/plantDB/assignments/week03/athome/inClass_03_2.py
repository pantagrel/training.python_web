import urllib
import urllib2

from pprint import pprint

base = 'http://maps.googleapis.com/maps/api/geocode/json'
addr = '1700 7th Ave, Seattle, WA 98101'
data = {'address': addr, 'sensor': False}
query = urllib.urlencode(data)
res = urllib2.urlopen('?'.join([base, query]))
response = json.load(res)
pprint(response)

