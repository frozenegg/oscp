#!/usr/bin/python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst"192.168.2.109", , hwdst="b0:05:94:82:25:db", psrc="192.168.2.1")
# setting op field to 2 to make this sent as arp response, not a request
