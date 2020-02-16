import socket

#AF=IPv4
#SOCK_STREAM for TCP/IP

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #set IP address and port
    s.bind(("127.0.0.1", 50007))
    #connect 1
    s.listen(1)
    #wait until connection
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                #receive data
                data = conn.recv(1024)
                if not data:
                    break
                print("data : {}, addr: {}".format(data, addr))
                #send data back to the client(b for byte)
                conn.sendall(b'Received: ' + data)
