from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('localhost', 50000))

def multiply(a, b):
	return a * b

server.register_function(multiply)

try:
	print "Use Ctrl-C to Exit"
	server.serve_forever()
except KeyboardInterrupt:
	print "Exiting"

server.register_instance(MyClass())

"""
1. what is class generation
2. what is [object] API
3. what is a 'service'? As in SOAP.
4. json.dumps(), json.loads()
	json.dump(file-like-object), json.load(file-like-object)
	.write, .read are both file-like (see: duck-typing)
"""

'https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderService_V03_01.asmx?wsdl')