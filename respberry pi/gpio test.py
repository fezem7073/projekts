#import RPi.lgpio
import RPI.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

while True:
    gpio.output(17, gpio.HIGH)
    print("led an")
    time.sleep(5)
    gpio.output(17, gpio.LOW)
    print("led aus")
    time.sleep(3)