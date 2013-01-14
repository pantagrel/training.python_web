import socket
import sys

# Create a TCP/IP socket
cFoo = socket.socket()
print 'socket', cFoo,'now created'

# HOST = '127.0.0.1'

# Bind the socket to the port
server_address = ('localhost', 50000)
try:
	cFoo.bind(server_address)
	print 'bind complete'
except socket.error, msg:
	print 'bind failed.'
	sys.exit()
print 'socket bind complete'

# Listen for incoming connections
cFoo.listen(5)
print 'listening...'

# Wait for a connection
conn,addr = cFoo.accept()
print 'connected with ', addr[0], ':', str(addr[1]

# # Receive the data and send it back
# msg = conn.recv(4096)
# conn.sendall(msg+msg)    
# 
# # Clean up the connection
# cFoo.close()