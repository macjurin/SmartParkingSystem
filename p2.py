import RPi.GPIO as GPIO
import time
from pynput.keyboard import Key,Listener

def motorspin(steps,spd):
    for x in range(steps):
        GPIO.output(i1, GPIO.HIGH)
        time.sleep(spd)
        GPIO.output(i1, GPIO.LOW)
        time.sleep(spd)

def direction(d):
    if d!=1 or d!=0:
        d=1
    GPIO.output(i2,d)

def drot(i1,i2,d):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    i1 = int(input("Pulse Pin :"))
    i2 = int(input("Direction Pin : "))
    GPIO.setup(i1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(i2, GPIO.OUT)
    direction(d)
    steps=int((400*90)/360)
    spd=0.0075
    motorspin(steps,spd)
    GPIO.cleanup()
