import socket                   # Import socket module
import select
import sys
import getimage as im
import train_model as tr
from _thread import *
import threading

data2=""
def on_new_client(conn,addr):
    data=conn.recv(1024)
    data=data.decode("utf-8").strip()
    file=data
    global  data2
    data2="students/"+data+".mp4"
    print(data)
    print(data2)
    with open(data2,'wb')as f:
        print('file opened')
        while True:
            data=conn.recv(1024)
            print('data=%s',(data))
            if not data:
                break
            else:
             f.write(data)

    print('Done sending')
    im.makeimage(file)
    tr.train(file)
    print ('Got connection from', addr)
    f.close()




port = 60000  
host = socket.gethostname()                  # Reserve a port for your service.
s = socket.socket()             # Create a socket object
     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5) 
while True:
                        # Now wait for client connection.
    print ("socket binded to %s" %(port)) 
    print ('Server listening....')
    print(socket.gethostbyname(socket.gethostname())) 
    conn, addr = s.accept()     # Establish connection with client.
    start_new_thread(on_new_client,(conn,addr))
    print ('Got connection from', addr)
    #data = conn.recv(1024)
    #print('Server received', data)

  
    #conn.send(bytes(repr('Thank you for connecting'), 'utf-8'))
conn.close()


