# client.py

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect(("127.0.0.2", port))
dd="fjasdf"
#s.send(dd.decode('utf-8'))
#s.send(bytes(repr(dd), 'utf-8'))

filename="ok.flv"
f=open(filename,'rb')

l=f.read(1024)

while(l):
    s.send(l)
    print('send',repr(l))
    l=f.read()

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
