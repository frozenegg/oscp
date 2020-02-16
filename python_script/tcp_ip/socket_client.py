import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #determine server
    s.connect(('127.0.0.1', 50007))
    #send server a message
    s.sendall(b'hello')
    #buffer size of the network is 1024
    #receive data from server
    data = s.recv(1024)
    print(repr(data))
