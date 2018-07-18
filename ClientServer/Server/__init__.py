import socket
import string
import sys
sys.path.append("..")
from Lib import server

sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = server.HOST
port = server.PORT
print (host)
print (port)
sSock.bind((host, port))

sSock.listen(5)
print ('server started and listening')

while 1:
    clientsocket, address = sSock.accept()
    try:
        print ('connection from ', address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = clientsocket.recv(1024).decode()
            # convert to lower case and strip all spaces
            exclude = set(string.punctuation)
            pal = ''.join((data.lower()).split())
            pal = ''.join(ch for ch in pal if ch not in exclude)
        
      
            print ('received "%s"' % data)
            print ('compressed to "%s"' % pal)
            if pal == pal[::-1]:
                    print ('Good Palindrome!')
                    clientsocket.send('yes'.encode())
            else:
                    print ('Not a Palindrome!')
                    clientsocket.send('no'.encode())
            
    finally:
        # Clean up the connection
        clientsocket.close()
