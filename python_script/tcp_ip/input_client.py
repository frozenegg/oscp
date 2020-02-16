import socket

ip_input = input('ip\n >> ')
port_input = input('port\n >> ')
message_raw_input = input('message\n >> ')

message_input = message_raw_input.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #determine server
    s.connect((ip_input, int(port_input)))
    #send server a message
    s.sendall(message_input)
    #buffer size of the network is 1024
    #receive data from server
    data = s.recv(1024)
    print(repr(data))
