""" This is a python 2 script to launch a flask server and communicate with Alexa through Flask-Ask. When it receives commands it uses the AlexaLamp class to 
send commands to the mood lamp attatched to the Raspberry Pi. Relies on ngrok to be run in a seperate terminal to open up a secure route from the local host to outside internet."""

from flask import Flask 
from flask_ask import Ask, statement 
import requests 
import json 
import threading
import math
import time
import datetime
import unicornhat as unicorn


class AlexaLamp():
    def __init__(self):
        self.light_on = False
        self.display_cleared = False
        self.stop_thread = False
        unicorn.set_layout(unicorn.PHAT)
        unicorn.rotation(0)
        unicorn.brightness(0.5)

    def start_rainbow(self):
        print "starting rainbow"
        self.light_on = True
        self.stop_thread = False
        self.display_cleared = False
        self.thread_obj = threading.Thread(target=self.rainbow)
        self.thread_obj.start()

    def stop_rainbow(self):
        print "stopping rainbow"
        self.light_on = False
        self.stop_thread = True
        self.display_cleared = True
        self.thread_obj.join()
        print "closed thread"

    def rainbow(self):
        i = 0.0
        offset = 30
        while not self.stop_thread:
            if self.light_on:
                i = i + 0.3
                for y in range(4):
                    for x in range(8):
                        r = 0#x * 32
                        g = 0#y * 32
                        xy = x + y / 4
                        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                        r = max(0, min(255, r + offset))
                        g = max(0, min(255, g + offset))
                        b = max(0, min(255, b + offset))
                        unicorn.set_pixel(x,y,int(r),int(g),int(b))
                unicorn.show()
                self.display_cleared = False
            else:
                if not self.display_cleared:
                    unicorn.clear()
                    unicorn.show()
                    self.display_cleared = True
            time.sleep(0.02)
        unicorn.clear()
        unicorn.show()

@ask.launch 
@ask.intent("lightOn") 
def on(): 
   print "light on"
   alexa_lamp.start_rainbow()
   return statement("Raspberry Pi Light turned on.") 

@ask.intent("lightOff") 
def off(): 
   print "light off"
   alexa_lamp.stop_rainbow() 
   return statement("Raspberry Pi Light turned off.") 

if __name__ == "__main__": 
    app = Flask(__name__) 
    ask = Ask(app, '/') 
    alexa_lamp = AlexaLamp()
    app.run(debug=True)
