import socket  # Import socket module

from threading import Thread
import subprocess

from _thread import *

import threading

#import attendence as att
import requests
import trial as tt

data2 = ""

def on_new_client(conn, addr):
    #start_new_thread(att.attendence, ())
    fac_id = conn.recv(1024)
    fac_id = fac_id.decode("utf-8").strip()
    print(fac_id)
    abc=fac_id.split(",")
     
    userdata = {"facid": abc[0], "time": abc[3], "subject": abc[1],"semester":abc[2]}
    resp = requests.post('http://127.0.0.1/attendence/mark_attendence.php', params=userdata)
    tt.attendence(abc[0],abc[3],abc[1],abc[2])
    #t1 = Thread(target=tt.attendence, args=(abc[0]))
    #t1.start()
    #t1.join()
    #att.attendence()
    #att.conn.close()
     
    print('Got connection from', addr)
 
    print("con.close")
    conn.close()
    


port = 40000
host = socket.gethostname()  # Reserve a port for your service.
s = socket.socket()  # Create a socket object
# Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(150)

while True:
    # Now wait for client connection.
    print("socket binded to %s" % (port))
    print('Server listening....')
    print(socket.gethostbyname(socket.gethostname()))
    conn, addr = s.accept()  # Establish connection with client.
    start_new_thread(on_new_client, (conn, addr))
    #t1 = Thread(target=tt.attendence, args=())
    #t1.start()
    #t1.join()
    print('Got connection from', addr)
    # data = conn.recv(1024)
    # print('Server received', data)
    # conn.send(bytes(repr('Thank you for connecting'), 'utf-8'))
print("closed")
conn.close()


