import urllib2
from bs4 import BeautifulSoup

#lxml is hands-down the god-king of html parsers
# the stuff below has happened once
# and doesn't need repeating. in same dir as this file
"""
page = urllib2.urlopen('http://tinyurl.com/osfeeds')
print page, page.code, page.headers['content-type'], page.headers['content-length']
html = page.read()
print len(html)
fh = open('blogScrape.html', 'w')
fh.write(html)
fh.close()
"""
# how to get going with a new virtualenv env
"""
have a folder <virtualenv> with source.
run this from terminal when a new virtualenv is needed.
$python virtualenv.py [options] <env>
[options: --distribute <foldername>]

to add new libraries,
activate the env (source <foldername>/bin/activate)
$pip install [whatever] (beautifulsoup4, html5lib, e.g.)
"""


def soupScrape(pageToParse):
	fh = open(pageToParse , 'r')
	parsed = BeautifulSoup(fh)
	entries = parsed.find_all('div', class_ = 'feedEntry')
	d = dict()
	d['pgsql'] = []
	d['django'] = []
	d['other'] = []
	for e in entries:
		anchor = e.find('a')
		paragraph = e.find('p', 'discreet')
		title = anchor.text.strip()
		url = anchor.attrs['href']
		try:
			source = paragraph.text.strip()
		except AttributeError:
			source = 'Uncategorized' 
		#should i lowercase every entry, just incase?
		#lowercasing goes here
		if 'Django' in source:
			d['django'].append(title)
		elif 'PostgreSQL' in source:
			d['pgsql'].append(title)
		else:
			d['other'].append(title)
		# print "SOURCE \n\r", source
		# print "TITLE \n\r", title
	print '\n\rPOSTGRES\n', d['pgsql']
	print '\n\rDJANGO\n', d['django']
	print '\n\rOTHER\n', d['other'] 
	
# pgsql, django, other = soupScrape(parsedPage)
soupScrape('blogScrape.html')


"""
QUESTIONS:
1. Why call the function as shown in slide 34? 
(with the implied tuple?)
2. should the title and the url be combined in the dictionary value?
or should they be separate but related entries? cuz separate-but-related
is confusing.
3. 

"""
