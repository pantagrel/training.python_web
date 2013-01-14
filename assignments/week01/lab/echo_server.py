import socket
import sys

# Create a TCP/IP socket
moo = socket.socket()
print 'socket now created'

# HOST = '127.0.0.1'

# Bind the socket to the port
server_address = ('localhost', 50000)
moo.bind(server_address)
print 'bind complete'

# Listen for incoming connections
moo.listen(5)
print 'listening...'


conn,addr = moo.accept()
print 'connected with ', addr[0], ':', str(addr[1])

while True:
	# Wait for a connection
	try:
	# Receive the data and send it back
		msg = conn.recv(4096)
		sum = 0
		for c in msg:
			sum = sum + int(c)
		reply = str(sum)
		conn.sendall(reply)    
	finally:
	# Clean up the connection
		print 'connections closing'
		conn.close()
		moo.close()

		
"""ADDS VALUES, BUT DOESN'T SEEM TO CLOSE PROPERLY. THIS ERROR:
connections closing
connections closing
Traceback (most recent call last):
  File "echo_server.py", line 27, in <module>
    msg = conn.recv(4096)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 170, in _dummy
    raise error(EBADF, 'Bad file descriptor')
socket.error: [Errno 9] Bad file descriptor"""