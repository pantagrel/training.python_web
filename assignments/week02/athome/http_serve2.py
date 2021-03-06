#!/usr/bin/env python

import socket
import email.utils

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

def ok_response(body):
		firstline = "HTTP:/1.1 200 OK"
		header = "Content-Type: text/html"
		empty = ""
		date = email.utils.formatdate(localtime=True)
		resp = "\r\n".join([firstline, header, date, empty, body])
		return resp


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
        print "received: %s, sending it back"%data
        client.send(ok_response(html))    
        client.close()