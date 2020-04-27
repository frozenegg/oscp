#!/usr/bin/python

import requests
import re

def request(url):
    try:
        get_response = requests.get("http://" + url)
        return(get_response)
    except requests.exceptions.ConnectionError:
        pass

target_url = "kyoto-u.ac.jp"

# with open("subdomains_wordlist.txt", "r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         test_url = word + "." + target_url
#         # print(test_url)
#         response = request(test_url)
#         if response:
#             print("[+] Discovered subdomain --> " + test_url)

with open("directory_wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered directory --> " + test_url)
