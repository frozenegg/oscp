#!/usr/bin/python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.2.106", 4444))
listener.listen(0)
print("[+] Waiting for incoming connections")
listener.accept()
print("[+] Got a connection!")
