import socket  # Import socket module

from _thread import *
import markattend as mk
import threading

data2 = ""

confidence=1000
def on_new_client(conn, addr):
    data = conn.recv(1024)
    data = data.decode("utf-8").strip()
    file = data
    global data2
    data2 = "attendence/" + data + ".jpg"
    print(data)
    print(data2)
    with open(data2, 'wb')as f:
        print('file opened')
        while True:
            data = conn.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            else:
                f.write(data)
    
    mk.recognize(file,conn)
    global confidence
    #print(confident+" ---  ")
    
 
    
 
    print('Got connection from', addr)
    f.close()
    conn.close()


conn="null"

port = 50000
host = socket.gethostname()  # Reserve a port for your service.
s = socket.socket()  # Create a socket object
    # Get local machine name
print("****1")
s.bind((host, port))  # Bind to the port
s.listen(5)
print("sdasds")

def attendence():

    
    while True:
        try:
            global conn
            # Now wait for client connection.
            print("socket binded to %s" % (port))
            print('Server listening....****')
            print(socket.gethostbyname(socket.gethostname()))
            conn, addr = s.accept()  # Establish connection with client.
            start_new_thread(on_new_client, (conn, addr))
            print('Got connection from', addr)
            # data = conn.recv(1024)
            # print('Server received', data)
        except:
            conn.close();

        # conn.send(bytes(repr('Thank you for connecting'), 'utf-8'))
    conn.close()

