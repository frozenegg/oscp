#!/usr/bin/python

import scapy.all as scapy
# scapt compatible with python2
# or do "pip3 install scapy-python3"

def scan(ip):
    # # ARP request
    # arp_request = scapy.ARP()
    # # scapy.ls(scapy.ARP()) to see what we need to put in the bracket, and we can see it is "pdst"
    # arp_request.pdst=ip
    # # or we can set the following:
    # # arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # print(arp_request.summary())
    #
    # # making sure arp request is sent to all the devices in the same network
    # # data is sent using MAC address, not the ip address
    # # MAC address is the physical address
    # broadcast = scapy.Ether()
    # #scapy.ls(scapy.Ether())
    # broadcast.dst="ff:ff:ff:ff:ff:ff" #this MAC address is vrtual, hence broadcast
    # broadcast.show()
    # print(broadcast.summary())

    # combination
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request #"/" appends data
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # srp allows us to send packets with a custom Ether part
    # sr returns two variables
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    # print(answered_list.summary())

    # print("IP\t\t\tMAC ADDRESS\n-------------------------------------------------")
    clients_list = []
    for element in answered_list:
        # print(element[1].show()) #without .show() prints raw data,which does not make sense
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    print(clients_list)

scan("192.168.2.1/24")
