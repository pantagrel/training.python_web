#!/usr/bin/python

import re
from cgi import escape, parse_qs
import bookdb
from wsgiref.simple_server import make_server

books = bookdb.BookDB()

# one function lists all books
def index(environ, start_response):
	"""this page shows the list of books as links"""
	links = ''
	for entry in books.titles():
# 		make a link with book title
# 		bookID = "/?id=" +str(entry['id']
		links += '<p><a href="/?id=' + entry['id'] + '">' + str(entry['title']) + '</p>'
	start_response('200 OK', [('Content-Type', 'text/html')])
	header = "<html><head><title>Kristin Gannon | Book Database Thingamajig</title></head>"
	body = "<body><h1>Book Database:</h1>%s</body></html>" % links
	return [header + body]


# one function lists one book
#generate a page called idX
def bookPage():
	header = "<head><title> %s </title></head>" % entry['id']
	return [header]

#not found
def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']
    
# map urls to functions
urls = [
    (r'^$', index),
    (r'/?$', bookPage),
    (r'/(.+)$', bookPage)   
]

    
def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)
		
if __name__ == '__main__':
	srv = make_server('localhost', 8080, application)
	srv.serve_forever()

