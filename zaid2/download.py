#!/usr/bin/python

import requests

def download(url):
    get_response = requests.get(url)
    # print(get_response.content) -> get raw file as seen in scapy
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file: # b for binary file
        out_file.write(get_response.content)

# laZagne


download("")
