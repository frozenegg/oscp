#!/usr/bin/python

import subprocess
import optparse
import re

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-n", "--new_mac", dest="new_mac", help="New MAC address you want to change to")

(options, arguments)= parser.parse_args()

# interface = input("choose interface\n >> ")
# new_mac = input("change mac address to:\n >> ")

interface = options.interface
new_mac = options.new_mac

#subprocess.call("ifconfig", shell=True)

#this one can be manipulated to run unintended commands
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

#this one only allows options
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

#if you get the following error:
#NameError: name 'eth0' is not defined
#it is because this is python3 module


ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

#Regex pythex
mac_address_search_result = re.search(r"\w\w:\w\w", ifconfig_result)
print(mac_address_search_result.group(0))
