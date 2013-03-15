#!/usr/bin/env python

import socket 
import os 
import glob
import email.utils

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

#2
def ok_response(body):
		firstline = "HTTP:/1.1 200 OK"
		header = "Content-Type: text/html"
		empty = ""
		date = email.utils.formatdate(localtime=True)
		resp = "\r\n".join([firstline, header, date, empty, body])
		return resp

#3
def parse_request(request):
	if request[0:3] == 'GET':	
		start = request.find('/')
		end = request.find('HTTP')
		# insert here: find all / characters
		if end == -1:
			return "ERROR: must be HTTP request"
		URI = str(request[start+1:end]) #"GET /index.html HTTP/1.1" -->strip this to just index.html
		if URI == '/ ' or URI == ' ':
			return 'what should i do with root/index'
		if URI[-2] == '/':
			URI = URI[:-2]
		return URI
	else:
		return "ERROR: must get an HTTP GET request"

#3.1
def client_error_response():
	#to be returned if parse_request fails
	#return APPROPRIATE_HTTP_CODE_FOR_ERRORS_AND_FAILS
	return None 

#4

contentDict = {
'plain': "Content-Type: text/plain",
'html' : "Content-Type: text/html",
'jpeg' : "Content-Type: image/jpeg",
'png' : "Content-Type: image/png",
'default' : "???",
}

responseDict = {
'200' : "HTTP:/1.1 200 OK",
'404' : "HTTP:/1.1 404 Not Found",
'501' : "HTTP:/1.1 501 Not Implemented (Coming Soon)",
}

def finduri(uri):
	uri = uri.strip()
	try:
		htmlfile = open(uri)
		html = htmlfile.read()
		htmlfile.close()
		return html
	except FileNotFoundError:
		return 'Cannot find requested file'	

def resolve_uri(uri):
	uri = uri.strip()
	if uri not in glob.glob('*'):
		return "HTTP:/1.1 404 Not Found"
	if os.path.isfile(uri):
		firstline = responseDict['200']
		header = 'PLACEHOLDER'
		empty = ""
# 		html = "PLACEHOLDER2"	
# could make all these string cases into a dictionary? to be separate, and cleaner?
		if uri[-5:] == '.html':
			header = contentDict['html']
			resp = "\r\n".join([firstline, header, empty])
			return resp
		elif uri[-4:] == '.txt':
			header = contentDict['plain']
			resp = "\r\n".join([firstline, header, empty])
			return resp
		elif uri[-5:] == '.jpeg' or uri[-4:] == '.jpg':
			header = contentDict['jpeg']
			resp = "\r\n".join([firstline, header, empty])	
			return resp
		elif uri[-4:] == '.png':
			header = contentDict['png']
			resp = "\r\n".join([firstline, header, empty])
			return resp
		else:
			header = contentDict['default']
			resp = "\r\n".join([firstline, header, empty])
			return resp
	elif os.path.isdir(uri):
		return responseDict['200']
	elif not os.path.isfile(uri):
		return responseDict['404']
	elif not os.path.isdir(uri):
		return responseDict['404']
	else:
		return responseDict['404']

#4.1
def notFound_response():
	#kinda already do this in #4?
	return None 

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

htmlfile = open("tiny_html.html")
html = htmlfile.read()
htmlfile.close()

while True: # keep looking for new connections forever
	client, address = s.accept() # look for a connection
	data = client.recv(size)
	if data: # if the connection was closed there would be no data
		print "\r\nReceived this from browser:\r\n %s \r\nSending it back" % data
		client.send(ok_response(html))
		log = parse_request(data)
		print "URI requested is %s " % log
		resolveLog = resolve_uri(log)
		print resolveLog
		client.close()