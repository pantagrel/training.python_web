#!/usr/bin/python

import re
from cgi import escape, parse_qs
from bookdb import BookDB
from wsgiref.simple_server import make_server



# map urls to functions
urls = []

books = BookDB()

	
# one function lists all books
# one function lists one book

def getBookTitles():
	html = """<html>
	<head><title>Book Database</title></head>
	<body>
	<h1>Book Database:</h1>
	%s
	</body>
	</html>"""
	for entry in books.titles():
		return entry
	html % entry

def application(environ, start_response):
	parameters = parse_qs(environ.get('QUERY_STRING', ''))
# 	I HAVE NO IDEA
# 	I HAVE NO IDEA
# 	I HAVE NO IDEA
# 	I HAVE NO IDEA
# 	I HAVE NO IDEA
# 	I HAVE NO IDEA

		
if __name__ == '__main__':
	srv = make_server('localhost', 8080, application)
	srv.serve_forever()

