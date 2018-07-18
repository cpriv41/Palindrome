import socket
import sys
sys.path.append("..")
from Lib import server

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (server.HOST, server.PORT)
print ('connecting to %s port %s' % server_address);
try:
	sock.connect(server_address)
# print('Enter Palindrome for testing: ')
	while 1:
		# Read the next palindrome
		inputdata = input('Enter Palindrome for testing: ')
		# Send data
		print ('Client sending "%s"' % inputdata)
		sock.send(inputdata.encode())

		# Look for the response
		data = sock.recv(1024).decode()
		print ('received "%s"' % data)
		if data == "yes":
			print ('Good Palindrome!')
		elif data == "no":
			print ('Not a palindrome.')
		else:
			print ('Not sure what happened!')
			break

finally:
	print ('closing socket')
	sock.close()

