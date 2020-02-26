#!/usr/bin/python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())
    scapy.ls(scapy.ARP())

scan("192.268.2.1/24")
