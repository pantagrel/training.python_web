import socket
import sys

# Create a TCP/IP socket
foo = socket.socket()

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)

foo.connect(server_address)

try:
# Send data
	num1 = raw_input('--> ')
	num2 = raw_input('--> ')
	message = num1 + num2
	foo.sendall(message)

# print the response
	reply = foo.recv(4096)
	print reply
finally:
	# close the socket to clean up
	print 'client is closed'
	foo.close()
