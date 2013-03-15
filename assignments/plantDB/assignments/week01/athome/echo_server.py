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
			#handle the fact that there's a comma in there.
		reply = str(sum)
		conn.sendall(reply)  
		print 'sent'  
		conn.close()
		moo.close()
	finally:
		sys.exit()
# 	Clean up the connection
		# conn.shutdown(1)
# 		moo.shutdown(1)
	# 	conn.close()
# 		moo.close()
# 		print 'server connections closing'